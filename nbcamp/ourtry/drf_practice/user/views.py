from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User as UserModel
from user.serializers import UserSeiralizer

# Create your views here.
class UserView(APIView):
    def get(self, request):
        return Response("HTTP METHOD GET")
    
    # 회원가입
    def post(self, request):
        serializer = UserSeiralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        target_user = UserModel.objects.last()
        target_user = {"fullname" : target_user.fullname,
                       "email" : target_user.email}
        return Response(target_user)
    def put(self, request):
        return Response("HTTP METHOD PUT")
    def delete(self, request):
        return Response("HTTP METHOD DELETE")
    
class UserSignView(APIView):
    
    def get(self, request):
        return Response("HTTP METHOD GET")
    
    # 로그인
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        me = authenticate(request, username=username, password=password)
        print(f"me->{me}")
        if not me:
            return Response("유저가 없습니다.")
        login(request, me)
        
        return Response(f"로그인 성공! 환영합니다. {username}님")
    def put(self, request):
        return Response("HTTP METHOD PUT")
    
    # 로그아웃
    def delete(self, request):
        user = request.user
        logout(request)
        return Response(f"로그아웃 되었습니다.{user}님 안녕히가세요!")