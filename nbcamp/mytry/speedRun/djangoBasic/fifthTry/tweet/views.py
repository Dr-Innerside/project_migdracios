from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')

def tweet(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user: # 만약 로그인이 되어 있다면
            return render(request, 'tweet/home.html')
        else:
            return redirect('/sign-in')
