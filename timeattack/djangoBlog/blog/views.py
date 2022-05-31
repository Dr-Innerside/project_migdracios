from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Article


# Create your views here.
def new_article(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        content = request.POST.get('content')

        new_post = Article()
        new_post.title = title
        new_post.category = Category.objects.get(name=category)
        new_post.content = content
        new_post.save()
        return HttpResponse(f'title{title}, category{category}, content{content}')

def view_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'category.html', {'categories': categories})