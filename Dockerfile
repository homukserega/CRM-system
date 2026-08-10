# ============================================
# STAGE 1: Builder
# ============================================
FROM python:3.12-alpine AS builder

RUN apk add --no-cache \
    postgresql-dev \
    gcc \
    musl-dev \
    libffi-dev \
    curl \
    && pip install --upgrade uv

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=crm.settings

WORKDIR /app

# Копируем pyproject.toml и устанавливаем зависимости
COPY pyproject.toml ./
COPY ./crm/ ./crm/

RUN uv venv /app/venv && \
    . /app/venv/bin/activate && \
    uv pip install --no-cache --group production && \
    # Собираем статику сразу в builder
    python /app/crm/manage.py collectstatic --noinput

# ============================================
# STAGE 2: Production
# ============================================
FROM python:3.12-alpine AS production

RUN apk add --no-cache \
    postgresql-client \
    libpq \
    && rm -rf /var/cache/apk/*

ENV PYTHONUNBUFFERED=1 \
    PATH="/app/venv/bin:${PATH}" \
    VIRTUAL_ENV="/app/venv"

WORKDIR /app

# Копируем виртуальное окружение
COPY --from=builder /app/venv /app/venv

# Копируем код и собранную статику
COPY --from=builder /app/crm /app/crm

# Создаем пользователя
RUN addgroup -g 1000 -S appuser && \
    adduser -u 1000 -S appuser -G appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["gunicorn", "--chdir", "/app/crm", "crm.wsgi:application", "--bind", "0.0.0.0:8000"]
