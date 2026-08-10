from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from ads.models import Ad
from contracts.models import Contract
from customers.models import Customer
from leads.models import Lead
from products.models import Product


class Command(BaseCommand):
    help = "Создаёт группы и назначает разрешения для ролей"

    def handle(self, *args, **options):
        # Создаём группы
        operator_group, _ = Group.objects.get_or_create(name="Оператор")
        marketer_group, _ = Group.objects.get_or_create(name="Маркетолог")
        manager_group, _ = Group.objects.get_or_create(name="Менеджер")

        # Получаем все разрешения для моделей
        def get_perms(model, codenames):
            ct = ContentType.objects.get_for_model(model)
            return Permission.objects.filter(content_type=ct, codename__in=codenames)

        # Назначаем разрешения для Оператора
        operator_perms = get_perms(Lead, ["view_lead", "add_lead", "change_lead", "delete_lead"])
        operator_group.permissions.set(operator_perms)

        # Назначаем разрешения для Маркетолога
        marketer_perms = list(
            get_perms(Product, ["view_product", "add_product", "change_product", "delete_product"])
        )
        marketer_perms += list(get_perms(Ad, ["view_ad", "add_ad", "change_ad", "delete_ad"]))
        marketer_group.permissions.set(marketer_perms)

        # Назначаем разрешения для Менеджера
        manager_perms = list(get_perms(Lead, ["view_lead", "change_lead"]))
        manager_perms += list(get_perms(Customer, ["add_customer", "view_customer"]))  # для перевода в активные
        manager_perms += list(
            get_perms(
                Contract,
                [
                    "view_contract",
                    "add_contract",
                    "change_contract",
                    "delete_contract",
                ],
            )
        )
        manager_group.permissions.set(manager_perms)

        # Всем группам даём разрешение на просмотр статистики рекламных кампаний
        view_ad_perm = Permission.objects.get(codename="view_ad", content_type__model="ad")
        for group in [operator_group, marketer_group, manager_group]:
            group.permissions.add(view_ad_perm)

        self.stdout.write(self.style.SUCCESS("Роли успешно настроены"))
