from rest_framework import serializers
from rest_framework import serializers

from .models import Ad


class AdSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=255,
        help_text = "Макс длина строки 255 симв.",
    )
    promotion = serializers.CharField(
        max_length=255,
        help_text = "Макс длина строки 255 симв.",
    )
    budget = serializers.DecimalField(
        max_digits=10,
        min_value=0,
        decimal_places=2,
        max_value=99999999,
        help_text="Стоимость рекламы (от 0 до 99 999 999.99). Пример: 1500.00.",
    )

    class Meta:
        model = Ad
        fields = "__all__"
