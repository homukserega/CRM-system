# CRM-система

#### Необходимые компоненты:
* python
* Docker
* poetry

## Установка виртуального окружения

> poetry config virtualenvs.create true

> poetry sync --all-groups

## Настройка БД

1. Скопировать env-template в .env
> cp env-template .env

2. Настроить необходимые параметры для своей БД в файле <b>.env</b>

 * Зaпуск БД
> docker compose up build -d

*  Остановка БД
> docker compose down -v

## Работа приложения
 * Запуск

из каталога crm/ выполнить команду

> python manage.py runserver 0.0.0.0:8000
 * Выполнение миграций БД

из каталога crm/ выполнить команду

> python manage.py migrate

# ДЕРЖИТЕ В КУРСЕ ДЕЛА