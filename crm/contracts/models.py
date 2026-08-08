from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone


class Contract(models.Model):
    """
    Модель контракта с клиентом.
    Хранит информацию о заключённом договоре, включая услугу, даты,
    стоимость и прикреплённый файл.
    """
    class Meta:
        """Дополнительные настройки модели."""
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
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        """
        Возвращает строковое представление контракта.
        Используется в админке и при выводе объектов.
        """
        return str(self.name or f"Контракт #{self.pk}")

    def get_absolute_url(self) -> str:
        """Возвращает абсолютный URL для просмотра деталей контракта."""
        return reverse('contracts:detail', args=[str(self.pk)])

    def is_active(self) -> bool:
        """Проверяет, активен ли контракт (не истёк)."""
        return self.end_date is None or self.end_date >= timezone.now()
