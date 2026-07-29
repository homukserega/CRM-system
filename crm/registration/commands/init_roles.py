from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from myapp.models import Client, Service, AdCampaign, Contract


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Группа "Оператор" – работа с клиентами
        operator_group, _ = Group.objects.get_or_create(name='Оператор')
        client_ct = ContentType.objects.get_for_model(Client)
        perms = Permission.objects.filter(content_type=client_ct,
                                          codename__in=['add_client', 'change_client', 'view_client'])
        operator_group.permissions.set(perms)

        # Группа "Маркетолог" – услуги и рекламные кампании
        marketer_group, _ = Group.objects.get_or_create(name='Маркетолог')
        service_ct = ContentType.objects.get_for_model(Service)
        ad_ct = ContentType.objects.get_for_model(AdCampaign)
        perms = Permission.objects.filter(content_type__in=[service_ct, ad_ct],
                                          codename__in=['add_', 'change_', 'view_', 'delete_'])
        marketer_group.permissions.set(perms)

        # Группа "Менеджер" – контракты + просмотр клиентов + кастомное разрешение
        manager_group, _ = Group.objects.get_or_create(name='Менеджер')
        contract_ct = ContentType.objects.get_for_model(Contract)
        perms = Permission.objects.filter(content_type=contract_ct,
                                          codename__in=['add_contract', 'change_contract', 'view_contract'])
        # Добавляем просмотр клиентов (view_client)
        view_client = Permission.objects.get(codename='view_client', content_type=client_ct)
        perms = list(perms) + [view_client]
        # Кастомное разрешение для перевода клиента в активные
        convert_perm, _ = Permission.objects.get_or_create(
            codename='can_convert_client',
            name='Может переводить клиента в активные',
            content_type=client_ct
        )
        perms.append(convert_perm)
        manager_group.permissions.set(perms)

        # Администратор – все права (можно не создавать группу, а использовать суперпользователя)
        # Но если хотите – добавьте все разрешения

        # Разрешение на просмотр статистики – даём всем группам
        stat_perm, _ = Permission.objects.get_or_create(
            codename='view_statistics',
            name='Может просматривать статистику'
        )
        for group in Group.objects.all():
            group.permissions.add(stat_perm)
           