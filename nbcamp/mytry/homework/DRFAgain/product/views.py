from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from product.models import Product

from .serializers import ProductSerializer
from datetime import datetime
from django.db.models.query_utils import Q

# Create your views here.

class ProductView(APIView):
    
    def get(self, request):
        query_data = Q(exposure_start_date__lte=datetime.now()) & Q(exposure_end_date__gte=datetime.now()) & Q(author=request.user) 
        products = Product.objects.filter(query_data)
        serializer = ProductSerializer(products, many=True).data
        return Response(serializer)

    # Product 생성 기능        
    def post(self, request):
        print(f"request->{request.data}")
        print(f"request type ->{type(request.data)}")
        request.data['author'] = request.user.id
        product_serializer = ProductSerializer(data=request.data)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Product 수정 기능        
    def put(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product_serializer = ProductSerializer(product, data=request.data, partial=True) 
        # 파샬은 내가 모든 데이터를 넣지 않아도 수정 허락해줌 수정하면서 봅시다 일단 없애놓고
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # 아 정답보고 잘썻다 꺼억


        
    def delete(self, request):
        return Response({"message":"제품 삭제!"})