from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Создаёт тестовых пользователей с ролями (оператор, маркетолог, менеджер, администратор)"

    def handle(self, *args, **options):
        # Список пользователей для создания
        users_data = [
            {
                "username": "admin",
                "password": "admin",
                "is_superuser": True,
                "is_staff": True,
                "groups": [],
                "email": "admin@test.com",
            },
            {
                "username": "operator",
                "password": "operator",
                "is_superuser": False,
                "is_staff": False,
                "groups": ["Оператор"],
                "email": "operator@test.com",
            },
            {
                "username": "marketer",
                "password": "marketer",
                "is_superuser": False,
                "is_staff": False,
                "groups": ["Маркетолог"],
                "email": "marketer@test.com",
            },
            {
                "username": "manager",
                "password": "manager",
                "is_superuser": False,
                "is_staff": False,
                "groups": ["Менеджер"],
                "email": "manager@test.com",
            },
        ]

        # Проверяем, что группы созданы (если нет — создаём)
        for data in users_data:
            for group_name in data["groups"]:
                Group.objects.get_or_create(name=group_name)

        for data in users_data:
            user, created = User.objects.get_or_create(
                username=data["username"],
                defaults={
                    "email": data["email"],
                    "is_superuser": data["is_superuser"],
                    "is_staff": data["is_staff"],
                },
            )
            # Устанавливаем пароль (хэшируется)
            user.set_password(data["password"])
            user.is_superuser = data["is_superuser"]
            user.is_staff = data["is_staff"]
            user.email = data["email"]
            user.save()

            # Назначаем группы
            user.groups.clear()
            for group_name in data["groups"]:
                group, _ = Group.objects.get_or_create(name=group_name)
                user.groups.add(group)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Создан пользователь: {user.username}"))
            else:
                self.stdout.write(f"Обновлён пользователь: {user.username}")

        self.stdout.write(self.style.SUCCESS("Тестовые пользователи успешно созданы/обновлены."))
