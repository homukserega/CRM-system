from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        # Добавляем пользователя в группу "Оператор" (по умолчанию)
        group, _ = Group.objects.get_or_create(name="Оператор")
        self.object.groups.add(group)
        return response
