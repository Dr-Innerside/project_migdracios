from django.db import models
from django.forms import CharField
from user.models import User as UserModel
from datetime import datetime

# Create your models here.

# 1. product라는 앱을 새로 생성해주세요
# 2. product 앱에서 <작성자, 제목, 썸네일, 설명, 등록일자, 노출 시작 일, 
# 노출 종료일>가 포함된 product 테이블을 생성해주세요


class Product(models.Model):
    author = models.ForeignKey(UserModel, verbose_name="작성자", on_delete=models.CASCADE) 
    title = models.CharField("제목", max_length=50)
    # 썸네일 파일 모델
    # 파일을 업로드할 위치 지정, 이 후 settings.py 에서 경로 설정해야함
    thumbnail = models.ImageField(upload_to='product/thumbnail/', verbose_name="썸네일", blank=True)
    desc = models.TextField("설명", max_length=50)
    post_date = models.DateTimeField("등록일자", auto_now_add=True)
    modified = models.DateTimeField("수정일자", auto_now=True)
    exposure_start_date = models.DateTimeField("게시 시작 일자", default =0)
    exposure_end_date = models.DateTimeField("게시 종료 일자", default =0)
    is_active = models.BooleanField("활성화 여부", default=True)
    price = models.IntegerField("가격")
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    choice_rating = (
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    )

    author = models.ForeignKey(UserModel, verbose_name="리뷰 작성자", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="상품", on_delete=models.CASCADE)
    content = models.TextField("내용")
    rate = models.IntegerField("평점", default=0, choices=choice_rating)
    post_date = models.DateTimeField("등록일자", auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.username}이 작성한{self.product.title}의 상품평"