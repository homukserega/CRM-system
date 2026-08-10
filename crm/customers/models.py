from django.conf import settings
from django.db import models


class Customer(models.Model):
    class Meta:
        verbose_name_plural = "Customers"

    lead = models.OneToOneField(
        settings.BASE_LEAD_MODEL,
        on_delete=models.CASCADE,
        related_name="customer",
    )
    contract = models.OneToOneField(
        settings.BASE_CONTRACT_MODEL,
        on_delete=models.CASCADE,
        related_name="customer",
    )
