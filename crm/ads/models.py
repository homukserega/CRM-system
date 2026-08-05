from django.db import models
from django.conf import settings


class Ad(models.Model):
    class Meta:
        verbose_name_plural = "Ads"

    name = models.CharField(max_length=255, blank=False, null=False, db_index=True)
    product = models.ForeignKey(
        settings.BASE_PRODUCT_MODEL,
        related_name="product",
        blank=True,
        on_delete=models.CASCADE,
    )
    promotion = models.CharField(max_length=255, null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
