from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sign_up_view(request):
    return HttpResponse("SIGN UP")

def sign_in_view(request):
    return HttpResponse('SIGN IN')