from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    # user/
    path('', views.UserView.as_view()),
]
