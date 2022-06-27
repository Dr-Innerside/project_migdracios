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
    post_date = models.DateTimeField("등록일자", default=datetime.today())
    exposure_start_date = models.DateTimeField("게시 시작 일자", default =0)
    exposure_end_date = models.DateTimeField("게시 종료 일자", default =0)
    
    def __str__(self):
        return self.title