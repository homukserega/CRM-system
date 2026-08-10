FROM python:3.12-alpine

# Системные зависимости для PostgreSQL и сборки
RUN apk add --no-cache \
    postgresql-dev \
    gcc \
    musl-dev \
    libffi-dev \
    libpq \
    curl

# Установка uv
RUN pip install uv

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Копируем только pyproject.toml для генерации requirements.txt
COPY pyproject.toml ./

# Генерируем requirements.txt (без uv.lock)
RUN uv pip compile pyproject.toml -o requirements.txt --no-cache

# Устанавливаем зависимости через pip (без кэша)
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY ./crm/ ./crm/

EXPOSE 8000

CMD ["gunicorn", "--chdir", "/app/crm", "crm.wsgi:application", "--bind", "0.0.0.0:8000"]