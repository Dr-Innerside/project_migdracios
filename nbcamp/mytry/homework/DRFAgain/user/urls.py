from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserView.as_view()),
    path('api',views.UserAPIView.as_view()),
]