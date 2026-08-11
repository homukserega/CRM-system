from rest_framework import serializers

from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=255,
        help_text="Пример: example@email.com"
    )

    class Meta:
        model = Lead
        fields = "__all__"
