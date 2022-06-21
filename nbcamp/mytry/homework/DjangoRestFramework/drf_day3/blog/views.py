from unicodedata import category
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import Article as ArticleModel
from user.models import User as UserModel
from blog.models import Category as CategoryModel

from user.serializers import UserSerializer
from user.serializers import ArticleSerializer

from datetime import  datetime, timedelta
from django.utils import timezone

from day3.permissions import RegistedMoreThreeDays

# Create your views here.

class ArticleView(APIView):
    # 사용자 게시글 조회
    def get(self, request):
        # print(f"type model --> {type(Category)}")

        # print(f"dir->>{dir(request.user)}")
        user = request.user


        # print(f"user_join_date ->{user.join_date}")
        # print(f"timezone now->{user.join_date>timezone.now()-timedelta(days=3)}")


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

   

    # 블로그 포스팅
    def post(self, request):
        permission_classes = [RegistedMoreThreeDays]

         # 블로그 작성하기
        def make_post(**kwargs):
            # print(f"포스트 작성 진입 ->{kwargs}")
            ArticleModel.objects.create(
                author= UserModel.objects.get(username=kwargs['author']),
                title = kwargs['title'],
                content = kwargs['content']
            )
            new_post = ArticleModel.objects.last()
            target_category = CategoryModel.objects.get(category_name=kwargs['category'])
            # print(f"target_cate->{target_category}")
            new_post.category.add(target_category)
            # print(f"new_post -> {new_post.category.all()}")
            
            return new_post

        # print(f"request -> {request.data}")
        request.data['author']=request.user.username
        result = make_post(**request.data)
        
        return Response({"message": "WIP Blog Posting...", "blog":ArticleSerializer(result).data})




    def put(self, request):
        pass
    def delete(self, request):
        pass