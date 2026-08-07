from django.db import models
from django.conf import settings


class Contract(models.Model):
    class Meta:
        verbose_name_plural = 'Contracts'

    name = models.CharField(max_length=255, null=True, blank=True)
    product = models.ForeignKey(
        settings.BASE_PRODUCT_MODEL,
        related_name="contract",
        blank=True,
        on_delete=models.CASCADE,
    )
    file = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

