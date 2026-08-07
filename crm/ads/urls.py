from django.urls import path
from .views import (
    AdListView, AdDetailView, AdCreateView,
    AdUpdateView, AdDeleteView, AdStatisticView
)

app_name = 'ads'

urlpatterns = [
    path('', AdListView.as_view(), name='list'),
    path('statistic/', AdStatisticView.as_view(), name='statistic'),
    path('new/', AdCreateView.as_view(), name='create'),
    path('<int:pk>/', AdDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', AdUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='delete'),
]