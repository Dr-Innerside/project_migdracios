from django.http import HttpResponse
from django.shortcuts import render

def base_response(request):
    return HttpResponse("가장 처음에 하는 테스트 리턴")

def first_connect(request):
    return render(request, 'my_test.html')