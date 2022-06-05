from django.shortcuts import render
from .models import Category, Drink, Image

# Create your views here.
def show_category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})

def show_drink(request):
    return render(request, 'drink.html')

def show_drink_detail(request):
    return render(request, 'drink_detail.html')