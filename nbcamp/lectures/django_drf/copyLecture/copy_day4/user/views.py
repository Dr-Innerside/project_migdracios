from django.shortcuts import render
from user.models import UserProfile
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout
from django.db.models import F

from user.serializers import UserSerializer

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

from ai.permissions import RegistedMoreThanAWeekUser

# Create your views here.
def sum_(num1, num2):
    return num1 + num2

class UserView(APIView):
    # permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAdminUser]
    permission_classes = [RegistedMoreThanAWeekUser]

    # 사용자 정보 조회
    def get(self, request):
        # print(request.data)
        # sum_result = sum_(**request.data)

        user = request.user
        all_users = UserModel.objects.all() # 전체 회원을 대상

        # print(f"dir(user)->{dir(user)}")

        # 정참조
        # user_profile = UserProfile.objects.get(user=user)
        # hobbys = user_profile.hobby.all()

        # 역참조
        # 선언해주지 않은 userprofile을 사용해서 가져옴
        '''
        사용법 1. exclude & annotate
        '''
        # hobbys = user.userprofile.hobby.all()   # OneToOneField는 예외로 _set을 붙이지 않음
        # for hobby in hobbys:
        #     hobby_members = hobby.userprofile_set.exclude(user=user).annotate(username=F('user__username')).values_list('username', flat=True)
        #     hobby_members = list(hobby_members)
        #     print(f"hobby: {hobby.name} / hobby members : {hobby_members}")

        # return Response({"message": f"get method!"})

        '''
        사용법 2. Serializer
        '''
        # return Response(UserSerializer(user).data)
        return Response(UserSerializer(all_users, many=True).data) # 전체 유저를 대상
    
    # 회원가입
    def post(self, request):
        
        return Response({"message": "post method!"})
    
    # 회원 정보 수정
    def put(self, request):
        
        return Response({"message": "put method!"})
    
    # 회원 탈퇴
    def delete(self, request):
        
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

        # print(f"request.data->{request.data}")

        user = authenticate(request, username=username, password=password)
        # print(f"user->{user}")

        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})

        login(request, user)
        return Response({"message": "login success!"})
    
    def delete(self, request):
        logout(request)
        return Response({"message": "logout success!"})

