from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserView.as_view()),
    path('login/', views.UserAPIVIew.as_view()),
]
