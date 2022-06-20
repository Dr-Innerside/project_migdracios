from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ArticleView(APIView):
    # 사용자 게시글 조회
    def get(self, request):
        '''
        Serializer를 이용해
        로그인한 사용자의
        1. 게시글
        2. 댓글
        을 리턴해준다!
        '''
        return Response()
    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass