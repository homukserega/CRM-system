from django.db import models
from django.conf import settings


class Contract(models.Model):
    class Meta:
        verbose_name_plural = "Contracts"

    name = models.CharField(max_length=255, null=True, blank=True)
    product = models.ManyToManyField(
        settings.BASE_PRODUCT_MODEL,
        related_name="products",
        blank=True, null=True,
    )
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now=True)
    period = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
