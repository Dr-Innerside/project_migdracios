from cgi import print_exception
from pydoc import describe
from unicodedata import name
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField("상품의 이름", max_length=50)
    desc = models.CharField("설명", max_length=50)
    price = models.IntegerField("가격")
    join_date = models.DateTimeField("도입일", auto_now_add=True)
    is_active = models.BooleanField("active 여부", default=False)
    
class Subscribe(models.Model):
    purchase_date = models.DateTimeField("구매일", auto_now_add=True)
    sub_start_date = models.DateTimeField("구독시작일", auto_now=True)
    sub_end_date = models.DateTimeField("구독종료일", auto_now=True)