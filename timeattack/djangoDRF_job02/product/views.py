from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product as ProductModel
from .serializers import ProductSerializer


# Create your views here.
class ProductView(APIView):
    def post(self, request):
        return Response({})

    def get(self, request):
        target_product = ProductModel.objects.filter(is_active=request.data['is_active'])
        return Response(ProductSerializer(target_product).data)

    def put(self, request):
        return Response({})

    def delete(self, request):
        return Response({})

    