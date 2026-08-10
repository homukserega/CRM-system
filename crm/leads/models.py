from django.conf import settings
from django.db import models
from django.urls import reverse


class Lead(models.Model):
    class Meta:
        verbose_name_plural = "Leads"

    first_name = models.CharField(max_length=255, null=False, blank=True)
    last_name = models.CharField(max_length=255, null=False, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=255, null=False, blank=True, unique=True)
    ad = models.ForeignKey(
        settings.BASE_AD_MODEL,
        on_delete=models.CASCADE,
        related_name="ad",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("leads:detail", args=[str(self.pk)])
