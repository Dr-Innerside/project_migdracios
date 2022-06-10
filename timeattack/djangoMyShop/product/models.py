from django.db import models

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