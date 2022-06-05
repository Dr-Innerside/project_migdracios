from django.shortcuts import render
from .models import Category, Drink, Image

# Create your views here.
def show_category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})

def show_drink(request):
    if request.method == 'GET':
        return render(request, 'category.html')
    elif request.method == 'POST':

        categories = Category.objects.all()
        category = request.POST.getlist('category')
        print(f'category -> {category}')
        category = Category.objects.get(name=category[0])
        drinks = Drink.objects.filter(category=category)
        print(f'DRINK -> {drinks}')
        return render(request, 'drink.html', {'drinks': drinks, 'categories': categories})


def show_drink_detail(request, id):
    if request.method == 'GET':
        drink = Drink.objects.get(id=id)
        image = Image.objects.get(name=id)

        return render(request, 'drink_detail.html', {'drink': drink, 'image': image})