from django.urls import path
from .views import (
    ClientListView,
    ClientDetailView
)
from . import views


urlpatterns = [
    path('', ClientListView.as_view(), name='clients'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client-detail')
]
