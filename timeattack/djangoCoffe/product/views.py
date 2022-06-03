from django.shortcuts import render, redirect
from .models import Category, Drink

# Create your views here.
def first(request):
    categories = Category.objects.all()

    return render(request, 'category.html', {'categories': categories})