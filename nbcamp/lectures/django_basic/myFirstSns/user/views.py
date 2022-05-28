from django.shortcuts import render


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        
        return ''


def sign_in_view(request):
    return render(request, 'user/signin.html')