from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
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

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            # 회원가입 중복 방지
            # exist_user = UserModel.objects.filter(username=username)
            exist_user = get_user_model().objects.filter(username=username)
            if not exist_user:
                # new_user = UserModel()
                # new_user.username = username
                # new_user.password = password
                # new_user.bio = bio
                # new_user.save()
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')
            else:
                return render(request, 'user/signup.html')



def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # me = UserModel.objects.get(username=username)
        me = auth.authenticate(request, username=username, password=password)
        if me:
            # request.session['user'] = me.username
            auth.login(request, me)
            return HttpResponse(f"Welcome to Login! {me.username}")
        else:
            return redirect('/sign-in')
    elif request.method == 'GET':
        return render(request, 'user/signin.html')