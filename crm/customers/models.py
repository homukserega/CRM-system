from django.db import models
from django.conf import settings


class Customer(models.Model):
    class Meta:
        permissions = [
            ("view_customer", "Can view customer"),
            ("add_customer", "Can add customer"),
            ("change_customer", "Can change customer"),
            ("delete_customer", "Can delete customer"),
        ]


    customer = models.OneToOneField(
        settings.BASE_LEAD_MODEL,
        on_delete=models.CASCADE,
        related_name="customer",
    )
    contract = models.OneToOneField(
        settings.BASE_CONTRACT_MODEL,
        on_delete=models.CASCADE,
        related_name="contract",
    )
