from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Администратор'),
        ('operator', 'Оператор'),
        ('marketer', 'Маркетолог'),
        ('manager', 'Менеджер'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='operator')

    # При необходимости добавьте дополнительные поля
    def __str__(self):
        return self.username