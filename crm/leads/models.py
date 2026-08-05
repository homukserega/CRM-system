from django.db import models
from django.conf import settings
from django.urls import reverse


class Lead(models.Model):
    class Meta:
        permissions = [
            ("view_lead", "Can view lead"),
            ("add_lead", "Can add lead"),
            ("change_lead", "Can change lead"),
            ("delete_lead", "Can delete lead"),
        ]

    first_name = models.CharField(max_length=255, null=False, blank=True)
    last_name = models.CharField(max_length=255, null=False, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=255, null=False, blank=True, unique=True)
    ad = models.ForeignKey(
        settings.BASE_AD_MODEL,
        on_delete=models.CASCADE,
        related_name="ad",
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('leads:detail', args=[str(self.pk)])
