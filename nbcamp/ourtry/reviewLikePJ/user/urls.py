from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('like/<int:id>', views.check_like)
]
