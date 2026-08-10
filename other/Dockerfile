# ---- Этап 1: Установка зависимостей ----
FROM python:3.12-alpine AS builder

# Системные зависимости для сборки PostgreSQL и других пакетов
RUN apk add --no-cache \
    postgresql-dev \
    gcc \
    musl-dev \
    libffi-dev \
    libpq \
    curl

# Установка uv
RUN pip install uv

# Рабочая директория
WORKDIR /app

# Копируем только файлы с зависимостями для лучшего кэширования
COPY pyproject.toml ./

# Создаём виртуальное окружение и устанавливаем зависимости без группы dev
RUN uv venv /venv && \
    . /venv/bin/activate && \
    uv sync --no-dev --no-interaction

# ---- Этап 2: Финальный образ ----
FROM python:3.12-alpine

# Устанавливаем только необходимые системные библиотеки для выполнения (без средств сборки)
RUN apk add --no-cache libpq

# Копируем установленное виртуальное окружение из предыдущего этапа
COPY --from=builder /venv /venv

# Копируем исходный код проекта
COPY ./crm/ /app/crm/

# Устанавливаем переменные окружения для использования виртуального окружения
ENV PATH="/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=crm.settings

# Рабочая директория
WORKDIR /app

# Запускаем Gunicorn
CMD ["gunicorn", "--chdir", "/app/crm", "crm.wsgi:application", "--bind", "0.0.0.0:8000"]