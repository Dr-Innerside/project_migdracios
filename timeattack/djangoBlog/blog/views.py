from django.shortcuts import render
from django.http import HttpResponse
from .models import Category


# Create your views here.
def new_article(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    elif request.method == 'POST':
        print(f'request data ->{request.POST}')
        title = request.POST.get('title')
        category = request.POST.get('category')
        content = request.POST.get('content')

        print(f'title -> {title}')
        print(f'category -> {category}')
        print(f'content -> {content}')

        return HttpResponse(f'title{title}, category{category}, content{content}')

def view_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'category.html', {'categories': categories})