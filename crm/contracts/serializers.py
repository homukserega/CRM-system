from rest_framework import serializers

from .models import Contract


class ContractSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=255,
        help_text="Макс длина строки 255 симв.",
    )
    cost = serializers.DecimalField(
        max_digits=10,
        min_value=0,
        decimal_places=2,
        max_value=99999999,
        help_text="Стоимость контракта (от 0 до 99 999 999.99). Пример: 1500.00.",
    )

    class Meta:
        model = Contract
        fields = "__all__"
