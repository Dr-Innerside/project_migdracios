from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import UserModel
from django.contrib import auth

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        bio = request.POST.get('bio')

        if password == password2:
            exist_user = get_user_model().objects.filter(username=username, password=password)
            if exist_user:
                UserModel().objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')
            else:
                return render(request, 'user/signup.html')
        else:
            return render(request, 'user/signup.html')
def sign_in_view(request):
    if request.method == 'GET':
        return render(request, 'user/signin.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        me = auth.authenticate(request, username=username, password=password)
        if me:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/signin.html')

def sign_out(request):
    return ''