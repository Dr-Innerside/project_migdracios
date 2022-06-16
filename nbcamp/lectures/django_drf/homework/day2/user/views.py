from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response


def sum_numbers(num1, num2):
    return num1 + num2


# Create your views here.
class UserView(APIView):
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        # 사용자 정보 조회

        # request.data
        '''
        {
            'num1': 5,
            'num2': 10
        }        
        '''

        result = sum_numbers(**request.data)
        # return Response({'message': 'get method!'})
        return Response({'message':f'result number is {result}'})

    def post(self, request):
        # 회원가입
        return Response({'message': 'post method!'})

    def put(self, request):
        # 회원 정보 수정
        return Response({'message': 'put method!'})

    def delete(self, request):
        # 회원 탈퇴
        return Response({'message': 'delete method!'})

def user_view(request):
    if request.method == 'GET':
        pass