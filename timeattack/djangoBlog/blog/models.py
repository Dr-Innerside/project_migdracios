from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = 'Category'

    name = models.CharField(max_length=20, null=False)
    desc = models.CharField(max_length=50, null=False)

class Article(models.Model):
    class Meta:
        db_table = 'Article'

    title = models.CharField(max_length=20, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.CharField(max_length=256, null=False)

