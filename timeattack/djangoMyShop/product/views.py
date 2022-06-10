from django.shortcuts import render
from .models import Category

# Create your views here.
def show_cate(request):
    all_cate = Category.objects.all()
    return render(request, 'cate.html', {'categories': all_cate})
