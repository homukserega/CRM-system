from django.db import models
from django.urls import reverse


class Product(models.Model):
    class Meta:
        verbose_name_plural = "Products"
        permissions = [
            ("view_product", "Can view product"),
            ("add_product", "Can add product"),
            ("change_product", "Can change product"),
            ("delete_product", "Can delete product"),
        ]

    name = models.CharField(max_length=255, blank=False, null=False, db_index=True)
    description = models.TextField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail', args=[str(self.pk)])
