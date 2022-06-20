from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import login, logout, authenticate
from rest_framework.response import Response

# Create your views here.

class UserAPIVIew(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})
        login(request, user)
        return Response({"message": "login success"})

    def delete(self, request):
        logout(request)
        return Response({"message": "logout success"})
        