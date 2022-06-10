from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cate, name='show-cate'),
    path('category/<int:id>', views.show_products, name='show-product'),
    path('product/<int:id>', views.make_orders, name='make-orders')
]