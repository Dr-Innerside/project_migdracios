from django.forms import ValidationError
from rest_framework import serializers
from rest_framework.response import Response
from datetime import datetime



from .models import Product as ProductModel


class ProductSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        현재 시간이 노출 시작 일과 노출 종료 일의 사이에 있거나,
        로그인 한 사용자가 작성한 product 쿼리셋을 직렬화 해서
        리턴해주는 serializer를 만들어주세요
        """
        return data
        
        # def validate(self, data):
        #     exposure_end_date = data.get("exposure_end_date", "")
        #     if exposure_end_date and exposure_end_date < datetime.now().date():
        #         raise serializers.ValidationError(
        #             detail = {"error": "유효하지 않은 노출 종료 날짜입니다."},
        #         )
        # return data
        
        # 코드 강탈

        # post_date = data['post_date']
        # exposure_start_date = data['exposure_start_date']
        # exposure_end_date = data['exposure_end_date']
        
        # print(query_time)
        # if query_time:
        #     return data
        # else:
        #     raise ValidationError({
        #         "detail": "노출 기간에 해당되지 않습니다."
        #     })
        # else:
        #     print('강아지 단어가 없습니다.')
        # return data
    # def create(self, validated_data):
    #     return 
    # def update(self, instance, validated_data):
    #     return instance
    class Meta:
        model = ProductModel
        fields = "__all__"
        
        
