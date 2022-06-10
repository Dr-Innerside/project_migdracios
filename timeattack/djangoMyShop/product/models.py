from django.db import models
from user.models import UserModel
# Create your models here.
class Category(models.Model):
    class Meta:
        db_table='categories'
    def __str__(self):
        return self.category
    categories = models.CharField(max_length=30, null=False)

class Product(models.Model):
    class Meta:
        db_table = 'products'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(max_length=100)
    desc = models.TextField()
    price = models.CharField(max_length=10)
    stock = models.CharField(max_length=10)

class OrderStatus(models.Model):
    class Meta:
        db_table='order_status'

    buyer = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=10)

    def __str__(self):
        return self.product_name


class UserOrder(models.Model):
    class Meta:
        db_table = 'user_orders'
    buyer = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    order_time = models.DateTimeField(auto_now_add=True)
    total_price = models.CharField(max_length=10)
    discont_per = models.CharField(max_length=10)
    final_price = models.CharField(max_length=10)
    order_bool = models.CharField(max_length=10)

    def __str__(self):
        return self.buyer

class ProductOrder(models.Model):
    class Meta:
        db_table = 'product_orders'
    buyer = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)





