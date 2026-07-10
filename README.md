# CRM-system

<i>Для запуска БД Необходимо установить <b>Docker</b></i>

## Настройка БД
1. Скопировать env-template в .env:
> cp env-template .env
2. Настроить необходимые параметры для своей БД в файле <b>.env</b>
 * Зaпуск БД
> docker compose up build -d

*  Остановка БД
> docker compose down -v

## Запуск crm системы:
 * Запуск
> python crm/manage.py runserver 0.0.0.0:8000
 * Выполнение миграций
> python crm/manage.py migrate

# ДЕРЖИТЕ В КУРСЕ ДЕЛА