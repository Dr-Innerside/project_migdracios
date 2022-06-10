from django.contrib import admin
from .models import UserOrder, Product, Category, ProductOrder, OrderStatus
# Register your models here.
admin.site.register(Category)
admin.site.register(UserOrder)
admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(OrderStatus)