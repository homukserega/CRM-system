from rest_framework import serializers

from .models import Contract


class ContractSerializer(serializers.ModelSerializer):
    cost = serializers.DecimalField(
        max_digits=10,
        min_value=0,
        decimal_places=2,
        max_value=99999999,
        help_text="Стоимость контракта (от 0 до 99 999 999.99). Пример: 1500.00.",
    )
    start_date = serializers.DateField(help_text="Дата начала (Формат YYYY-MM-DD)")
    end_data = serializers.DateField(help_text="Дата окончания (Формат YYYY-MM-DD)",
                                     required=False, allow_null=True)

    class Meta:
        model = Contract
        fields = "__all__"
