from django.db import models



# Create your models here.

# 블로그 카테고리 모델
class Category(models.Model):
    category_name = models.CharField("카테고리 이름", max_length=50)
    category_desc = models.CharField("카테고리 설명", max_length=50)

    def __str__(self):
        return self.category_name