from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    # user/
    path('', views.UserView.as_view()), # CBV는 as_view()가 반드시 작성되어야 함!
    path('login/', views.UserAPIView.as_view()), # 로그인
]
