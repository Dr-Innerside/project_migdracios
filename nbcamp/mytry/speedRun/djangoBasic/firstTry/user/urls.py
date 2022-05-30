from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign_up_view'),
    path('sign-in/', views.sign_in_view, name='sign_in_view'),
]