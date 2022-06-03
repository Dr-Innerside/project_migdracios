from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='first'),
    path('drink/<int:id>', views.drink, name='drink'),
]