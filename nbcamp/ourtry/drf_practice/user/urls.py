from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserView.as_view()),
    path('sign/', views.UserSignView.as_view()),
]