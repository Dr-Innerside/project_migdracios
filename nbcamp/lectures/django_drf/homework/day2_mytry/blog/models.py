from tkinter import CASCADE
from unicodedata import category
from django.db import models
from matplotlib.pyplot import title

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10)
    desc = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey('user.User', verbose_name='author', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    category = models.ManyToManyField(Category, verbose_name="category")
    content = models.TextField()

    def __str__(self):
        return f'{self.title}--by.{self.author}'