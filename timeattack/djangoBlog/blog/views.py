from django.shortcuts import render


# Create your views here.
def new_article(request):
    if request.method == 'GET':
        render(request, 'new.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        content = request.POST.get('content')

        print(f'title -> {title}')
        print(f'category -> {category}')
        print(f'content -> {content}')

        return ''
