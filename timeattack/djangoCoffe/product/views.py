from django.shortcuts import render, redirect

# Create your views here.
def first(request):
    return render(request, 'category.html')