from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import permissions

from .serializers import ItemSerializer

# Create your views here.

class ItemView(APIView):
    permission_classes = [permissions.AllowAny]

    # 아이템 조회
    # item=?category=appliance
    def get(self, request):
        '''
        카테고리 밸류를 입력받아 아이템을 조회하기
        카테고리 아이템 변수 초기화
        아이템시리얼라이저(카테고리).data
        '''
        print("여기가 item get이에요!")
        print(request.GET)

        return Response(ItemSerializer(**request.GET).data)
        
    def post(self, request):
        return Response("method POST")
    def put(self, request):
        pass
    def delete(self, request):
        pass

