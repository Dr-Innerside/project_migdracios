from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_category, name='category'),
    path('drink/', views.show_drink, name='drink'),
    path('drink/detail', views.show_drink_detail, name='drink-detail'),
]