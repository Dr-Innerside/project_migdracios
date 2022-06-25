from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import Article as ArticleModel

from .serializers import UserSerializer, UserProfileSerializer


# Create your views here.

# 2일차 숙제 9번과제. CBV 기반으로 로그인 / 로구아웃 기능을 구현해주세요
class UserView(APIView):
    # 사용자 조회
    def get(self, request):
        print(request.user)
        # return Response("get 리퀘스트")
        return Response(UserSerializer(request.user).data)

        # **request.data 필요없지않나요? 유저 정보만 가져와서 보여주면되는데
        
    # 로그인
    def post(self, request):
        '''
        1. POSTMAN에서 사용자 아이디, 비밀번호를 입력
        2. request.data에서 입력 값을 받아 변수 초기화
        3. is.authenticated 조회
        4. login
        '''
        
        print(f"request.data->{request.data}")
        is_login = authenticate(request, **request.data)
        # print(f"is_login->{is_login}")
        if is_login:
            login(request, is_login)
            return Response(f"login성공! / {is_login} 님 환영합니다!")
        return Response("로그인 되어 있지 않습니다!")
        

        # 유저가 아닐 시 경우도 있어야함 옼키
        
                
    # 회원정보 수정
    def put(self, request):
        return Response("put 리퀘스트")
    # 로그아웃
    def delete(self, request):
        '''
        로그아웃 API
        간단하게 한줄 logout 사용하기
        '''
        user = request.user
        logout(request)
        
        return Response(f"로그아웃 되었습니다. / {user} 님 안녕히가세요!")
    
# 10. CBV 기반으로 로그인 한 사용자의 게시글의 제목을 리턴해주는 기능을 구현해주세요
class UserAPIView(APIView):
    # 사용자 게시글 제목을 리턴
    def get(self, request):
        print("="*30)
        print(f"APIVIEW GET")
        '''
        1. 로그인 한 사용자 변수 초기화
        2. 사용자 아이디로 Article 모델 조회
        3. 리턴
        '''
        user = request.user
        print(f"user->{user}")
        target_article = ArticleModel.objects.filter(author=user.id)
        print(f"target_article->{target_article}")
        return Response(f"get response && 작성한 게시글은~{target_article}")
    def post(self, request):
        return Response("post response")
    def put(self, request):
        return Response("put response")
    def delete(self, request):
        return Response("delete response")



