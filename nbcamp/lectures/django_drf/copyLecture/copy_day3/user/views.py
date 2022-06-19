from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout



# Create your views here.
def sum_(num1, num2):
    return num1 + num2

class UserView(APIView):
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        # 사용자 정보 조회
        print(request.data)
        sum_result = sum_(**request.data)
        return Response({"message": f"get method! && sum->{sum_result}"})
    def post(self, request):
        # 회원가입
        return Response({"message": "post method!"})
    def put(self, request):
        # 회원 정보 수정
        return Response({"message": "put method!"})
    def delete(self, request):
        # 회원 탈퇴
        return Response({"message": "delete method!"})

def user_view(request):
    if request.method == 'GET':
        return Response({"message": "get method!"})


class UserAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})

        login(request, user)
        return Response({"message": "login success!"})
    
    def delete(self, request):
        logout(request)
        return Response({"message": "logout success!"})

