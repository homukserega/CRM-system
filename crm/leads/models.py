from django.db import models


class Lead(models.Model):
    class Meta:
        verbose_name_plural = "Leads"

    first_name = models.CharField(max_length=255, null=False, blank=True)
    last_name = models.CharField(max_length=255, null=False, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=255, null=False, blank=True, unique=True)
