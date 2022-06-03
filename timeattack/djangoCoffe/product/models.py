from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = 'category'
    name = models.CharField(max_length=20)

class Drink(models.Model):
    class Meta:
        db_table = 'drink'
    name = models.CharField(max_length=20, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nutrition = models.CharField(max_length=20)
    allergy = models.CharField(max_length=20)