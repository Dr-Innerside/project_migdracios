from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table= 'categories'
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

class Drink(models.Model):
    class Meta:
        db_table = 'drinks'
    name = models.CharField(max_length=30, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nutrition = models.CharField(max_length=50, null=False)
    allergy = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Image(models.Model):
    class Meta:
        db_table = 'images'
    name = models.ForeignKey(Drink, on_delete=models.CASCADE)
    file_url = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.name