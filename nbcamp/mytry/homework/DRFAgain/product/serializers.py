from django.forms import ValidationError
from rest_framework import serializers
from rest_framework.response import Response
from datetime import datetime
from dateutil.tz import gettz
from django.db.models import Avg



from .models import Review as ReviewModel
from .models import Product as ProductModel

TODAY = datetime.now(gettz('Asia/Seoul'))

def avg_star(argument):
    argument = int(argument)
    switcher = {
        1: "★",
        2: "★★",
        3: "★★★",
        4: "★★★★",
        5: "★★★★★",
    }

    return switcher.get(argument, "nothing")

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField()
    def get_review(self, obj):
        print(f"OBJ DIR->{dir(obj)}")
        reviews = []
        for review in obj.review_set.all():
            review_data = {
                "review_id" : review.id,
                "review_content" : review.content,
                "review_rate" : review.rate
            }
            reviews = review_data
        return reviews
        #저는 그냥 AVG 썼습니다.
        #여기다가 쓰시면 안되요
        #문제가 뭐였죠 리턴아닌가요?
        
        '''
        5번 상품 정보를 리턴 할 때 상품에 달린 review와 평균 점수를 함께 리턴해주세요
        1. 평균 점수는 (리뷰 평점의 합/리뷰 갯수)로 구해주세요
        2. 작성 된 리뷰는 모두 return하는 것이 아닌, 가장 최근 리뷰 1개만 리턴해주세요
        '''
        
        # reviews=obj.review_set.all()
        # print(reviews)
        # print()
        # reviews=obj.review_set.all().aggregate(Avg('review'))
        # 
        # return {
            # "최근 리뷰" : ReviewSerializer(reviews.last())
        # }

        
    def validate(self, data):
        exposure_end_date = data.get("exposure_end_date", "")
        if exposure_end_date and exposure_end_date < TODAY:
            raise serializers.ValidationError(
                detail = {"error": "유효하지 않은 노출 종료 날짜입니다."},
            )
        return data
    
    def create(self, validated_data):
        desc = validated_data['desc']
        validated_data['desc'] = desc + f'\n{TODAY}에 등록된 상품 입니다.'
        product = ProductModel(**validated_data)
        product.save()
        # replace메서드를 사용하는 경우
        # product.desc += f"\n\n{product.post_date.replace(microsecond=0, tzinfo=None)}에 등록된 상품입니다."
        # product.save()
        return product
    
    def update(self, instance, validated_data):
        desc = validated_data['desc']
        validated_data['desc'] = desc + f'\n{TODAY}에 수정된 상품 입니다.'
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
        
    rating_avg = serializers.SerializerMethodField()
    # stars = ''
    def get_rating_avg(self, obj):
        try:
            rate_avg = obj.review_set.all().aggregate(avg=Avg('rate'))['avg']
        except:
            rate_avg = 0

        print('rate_avg ? ' + str(rate_avg))
        
        if rate_avg is not None:
            # for i in range(round(rate)):
            #     stars += ★
            # return stars
            
            if rate_avg <= 1: 
                star_avg = '★'
            elif rate_avg > 1 and rate_avg <=2:
                star_avg = '★★'
            elif rate_avg > 2 and rate_avg <=3:
                star_avg = '★★★'
            elif rate_avg > 3 and rate_avg <=4:
                star_avg = '★★★★'
            elif rate_avg > 4 and rate_avg <=5:
                star_avg = '★★★★★'
            return star_avg
        else:
            return "평점이 없습니다"

    class Meta:

        #여기다가 !!!
        #시리얼 라이즈 메소드 쓰면 되요!
        


        model = ProductModel
        fields = "__all__"
        
        
