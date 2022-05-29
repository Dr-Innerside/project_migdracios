from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            me = UserModel.objects.filter(username=username)
            if me:
                return redirect('/sign-up')
            else:
                new_user = UserModel()
                new_user.username = username
                new_user.password = password
                new_user.bio = bio
                new_user.save()
        return redirect('/sign-in')


def sign_in_view(request):
    if request.method == 'GET':
        return render(request, 'user/signin.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = UserModel.objects.get(username=username)
        if me.password == password:
            request.session['user'] = me.username
            return HttpResponse(f'{username} 님 환영합니다!')
        else:
            return redirect('/sign-in')