from django.shortcuts import render, redirect
from .models import Category, Drink

# Create your views here.
def first(request):
    categories = Category.objects.all()

    return render(request, 'category.html', {'categories': categories})

def drink(request, id):
    if request.method == 'GET':
        print(f'드링크로 넘어가랏!')
        category = Category.objects.get(id=id)
        drinks = Drink.objects.filter(category=category)
        print(f'해당하는 드링크는! {drinks}')
        return render(request, 'drink.html', {'drinks':drinks})

