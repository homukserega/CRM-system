from django.db import models
from django.urls import reverse


class Product(models.Model):
    class Meta:
        verbose_name_plural = "Products"

    name = models.CharField(max_length=255, blank=False, null=False, db_index=True)
    description = models.TextField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail', args=[str(self.pk)])
