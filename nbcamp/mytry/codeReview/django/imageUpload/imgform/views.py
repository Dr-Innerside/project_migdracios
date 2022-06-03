from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse


# Create your views here.
def home(request):
    return redirect('image_upload/')

#4번 views.py
def students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)#이미지는 request.FILES 리스트 오브젝트로 들어간다
        if form.is_valid():#이미지가 있는지, 에러가 없는지 확인해주는 함수
            form.save()
            return redirect('success')

    elif request.method == 'GET':
        form = StudentForm()
        return render(request, 'studentform.html', {'form': form})


def uploadok(request):
    return HttpResponse('업로드 성공')#여기까지 잘 뜬다