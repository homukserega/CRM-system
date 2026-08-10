from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["lead", "contract"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Поле customer можно сделать скрытым, если оно предзаполнено
        # или оставить видимым для выбора вручную (по ТЗ – предзаполнено)
        # Для предзаполнения используется initial в LeadToCustomerView
