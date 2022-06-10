from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def show_cate(request):
    all_cate = Category.objects.all()
    return render(request, 'cate.html', {'categories': all_cate})

def show_products(request, id):
    if request.method =='GET':
        all_cate = Category.objects.all()
        product_list = Product.objects.filter(category=id)
        return render(request, 'product.html', {'categories':all_cate, 'product_list': product_list})

def make_orders(request, id):
    if request.method == 'GET':
        item = request.GET
        print(f'product->{item}')
        item = Product.objects.get(name=item)

        return render(request, 'order.html', item)
