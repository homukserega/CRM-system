FROM python:3.12-alpine

# Устанавливаем системные зависимости
RUN apk add --no-cache \
    postgresql-dev \
    gcc \
    musl-dev \
    libffi-dev \
    libpq \
    curl

# Устанавливаем uv
RUN pip install uv

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml ./

# Генерируем requirements.txt из pyproject.toml и устанавливаем зависимости
RUN uv pip compile pyproject.toml -o requirements.txt && \
    uv pip install --system -r requirements.txt

# Копируем Необходимые данные
COPY ./crm/ ./crm/

COPY .env ./

# Собираем статику (позже она будет собрана при запуске, но можно и здесь)
# RUN python crm/manage.py collectstatic --noinput

EXPOSE 8000

# Точка входа: запуск gunicorn (команда переопределяется в docker-compose)
CMD ["gunicorn", "--chdir", "/app/crm", "crm.wsgi:application", "--bind", "0.0.0.0:8000"]