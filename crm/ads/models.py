from django.db import models
from django.conf import settings
from django.urls import reverse


class Ad(models.Model):
    class Meta:
        permissions = [
            ("view_ad", "Can view ad"),
            ("add_ad", "Can add ad"),
            ("change_ad", "Can change ad"),
            ("delete_ad", "Can delete ad"),
        ]

    name = models.CharField(max_length=255, blank=False, null=False, db_index=True)
    product = models.ForeignKey(
        settings.BASE_PRODUCT_MODEL,
        related_name="product",
        blank=True,
        on_delete=models.CASCADE,
    )
    promotion = models.CharField(max_length=255, null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ads:detail', args=[str(self.pk)])
