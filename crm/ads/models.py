from decimal import Decimal
from django.core.validators import MinValueValidator
from django.conf import settings
from django.db import models
from django.urls import reverse


class Ad(models.Model):
    class Meta:
        verbose_name_plural = "Ads"

    name = models.CharField(max_length=255, blank=False, null=False, db_index=True)
    product = models.ForeignKey(
        settings.BASE_PRODUCT_MODEL,
        related_name="ads",
        on_delete=models.PROTECT,
    )
    promotion = models.CharField(max_length=255, null=True, blank=True)
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ads:detail", args=[str(self.pk)])
