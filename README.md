# CRM-система

#### Необходимые компоненты:
* python
* Docker
* poetry

## Установка виртуального окружения

> poetry config virtualenvs.create true

> poetry sync --all-groups

## Настройка БД

1. Скопируйте env-template в .env
> cp env-template .env

2. Настройте необходимые параметры для своей БД в файле <b>.env</b>

 * Команда для запуска БД
> docker compose up build -d

*  Команда для остановки БД
> docker compose down -v

## Работа приложения
 * Перейдите в каталог crm/. Выполните команду для запуска приложения
> python manage.py runserver 0.0.0.0:8000

Выполните миграции, если необходимо

> python manage.py migrate

 * Сочетание клавиш для остановки приложения <b>Ctrl + C</b>


# ДЕРЖИТЕ В КУРСЕ ДЕЛА