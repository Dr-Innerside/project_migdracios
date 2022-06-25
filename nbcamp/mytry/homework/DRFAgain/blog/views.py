from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from blog.models import (
   Article as ArticleModel,
   Category as CategoryModel,
   Comment as CommentModel,
)

from user.serializers import ArticleSerializer

from ai.permissions import BasePermission
from ai.permissions import SamIll, IsRegister7DaysOrIsAdmin

# Create your views here.



class BlogView(APIView):

    #여기에 퍼미션 적용
   # permission_classes = [SamIll]
   permission_classes = [IsRegister7DaysOrIsAdmin]
   


   # 게시글 조회 API
   def get(self, request):
      
      '''
      3. article view에 게시글 조회 기능을 만들되, 
      현재 일자를 기준으로 노출 시작 일자와 노출 종료 일자 사이에 있는 항목들만 
      리턴해주도록 필터를 설정해주세요
       - 리턴 데이터는 게시글 작성일 기준으로 정렬하여 
       최근 쓴 글이 가장 먼저 올라오도록 해주세요
      '''
      today = timezone.now()
      article_list = ArticleModel.objects.filter(
         exposure_start_date__lte=today,
         exposure_end_date__gte=today).order_by('-id')
      print(f"article_list->{article_list}")
      
      # lte -->>> 노출시작일 (lte=작다면)<= today lte는 오른쪽으로 휘었어
      # gte -->>> 노출종료일 (get=크다면)>= today get는 왼쪽으로 휘었어
      # 아 부등호 개어려워 싫어 그만좀 비교해 이 더러운세상 ㅠ
      
      return Response(ArticleSerializer(article_list, many=True).data)
      # return Response(f"get method!! && {article_list}")


      
   
   # 게시글 작성 API
   def post(self, request):
      
    '''
      3일차 6번과제. blog 앱에 title / category / contents를 입력받아서 게시글을 작성하는 기능을 구현해주세요
      - 만약 title이 5자 이하라면 게시글을 작성할 수 없다고 리턴해주세요
      - 만약 contents가 20자 이하라면 게시글을 작성할 수 없다고 리턴해주세요
      - 만약 카테고리가 지정되지 않았다면 카테고리를 지정해야 한다고 리턴해주세요
   '''
   
    print(f"request->{request.data}")

    if len(request.data.get('title','')) <= 5:
        return Response("제목은 다섯 자 이하일 수 없습니다!")
    if len(request.data.get('content','')) <= 5:
       return Response("내용은 20자를 채워주세요!")
    if not request.data.get('category',[]):
       return Response("카테고리를 지정해주세요!")
    
    request.data['author'] = request.user
    category = request.data.pop('category')
   #  category = CategoryModel.objects.filter(id__in=category)
       
    print(f"category->{category}")
    new_article = ArticleModel.objects.create(**request.data)
    print(f"new_article->{new_article}")
    new_article.category.add(*category)

    return Response("저장됐니?")
 
   def put(self, request):
      return Response("put method!!")
   def delete(self, request):
      return Response("delete method!!")