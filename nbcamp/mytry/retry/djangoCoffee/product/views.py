from django.shortcuts import render

# Create your views here.
def show_category(request):
    return render(request, 'category.html')

def show_drink(request):
    return render(request, 'drink.html')

def show_drink_detail(request):
    return render(request, 'drink_detail.html')