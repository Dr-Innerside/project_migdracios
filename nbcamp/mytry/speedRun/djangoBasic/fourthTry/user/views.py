from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserModel
from django.contrib.auth import get_user_model
from django.contrib import auth


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        bio = request.POST.get('bio')

        exist_user = get_user_model().objects.filter(username=username)
        if not exist_user:
            if password == password2:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')
            else:
                return HttpResponse("비밀번호가 일치하지 않습니다")
        else:
            return HttpResponse("존재하지 않는 사용자 입니다")



def sign_in_view(request):
    if request.method == 'GET':
        return render(request, 'user/signin.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        me = auth.authenticate(request,username=username, password=password)
        if me:
            auth.login(request, me)
            return HttpResponse(f"LOGIN welcome {me.username}")
        else:
            return render(request, 'user/signin.html')
