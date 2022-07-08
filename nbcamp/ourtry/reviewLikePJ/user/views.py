from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth

from .models import User as UserModel
from .models import Like as LikeModel

# Create your views here.
def home(request):
    if request.method == 'GET':
        print(f"request_user{request.user}")
        return render(request, 'index.html', {"user":request.user})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('password')
        
        check_user = UserModel.objects.filter(username=username)
        print(f"check_user-->{check_user}")
        if not check_user:
            new_user = UserModel()
            new_user.username = username
            new_user.passowrd = password
            new_user.save()
            return redirect('/user/signin')
        return HttpResponse("이미 가입한 유저가 있습니다.")
        
    if request.method == 'GET':
        return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('password')
        print(f"username {username} / password {password}")
        
        all_user = UserModel.objects.all()
        print(f"all_user->{all_user}")
        
        user = UserModel.objects.get(username=username)
        print(f"user->{user}")
        if user:
            auth.login(request, user)
            return redirect('/user')
        return redirect('/user/signin')
            
    if request.method == 'GET':
        return render(request, 'signin.html')
    
def check_like(request, id):
    if request.method =='POST':
        me = request.user
        print(f"me-->{me}")
    
    if request.method =='GET':
        return render(request, 'index.html')