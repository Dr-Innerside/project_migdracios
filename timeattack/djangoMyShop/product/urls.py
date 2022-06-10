from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cate, name='show-cate'),
    path('category/<int:id>', views.show_products, name='show-product'),
]