from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserModel


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        bio = request.POST.get('bio')

        exist_user = UserModel.objects.filter(username=username)
        if exist_user:
            if password == password2:
                new_user = UserModel()
                new_user.username = username
                new_user.password = password
                new_user.bio = bio
                new_user.save()
                return redirect('/sign-in')
            else:
                return HttpResponse("비밀번호가 일치하지 않습니다")
        else:
            return HttpResponse("존재하지 않는 사용자 입니다")



def sign_in_view(request):
    return ''
