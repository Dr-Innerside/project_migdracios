from django.contrib import admin
from .models import Category, Drink, Image

# Register your models here.
admin.site.register(Category)
admin.site.register(Drink)
admin.site.register(Image)