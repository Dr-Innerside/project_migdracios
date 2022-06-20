from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import Comment, Category

from user.serializers import UserSerializer
from user.serializers import ArticleSerializer

# Create your views here.

class ArticleView(APIView):
    # 사용자 게시글 조회
    def get(self, request):
        print(f"type model --> {type(Category)}")

        # print(f"dir->>{dir(request.user)}")
        user = request.user
        target_article = user.article_set.all()[0]
        # print(f"아티클셋->{target_article}")
        '''
        Serializer를 이용해
        로그인한 사용자의
        1. 게시글
        2. 댓글
        을 리턴해준다!
        '''
        # return Response(ArticleSerializer(request.user).data)
        return Response((ArticleSerializer(target_article)).data)
    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass