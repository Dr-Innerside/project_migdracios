from turtle import title
from unicodedata import category
from django.db import models

from user.models import User


# Create your models here.

# 블로그 카테고리 모델
class Category(models.Model):
    category_name = models.CharField("카테고리 이름", max_length=50)
    category_desc = models.CharField("카테고리 설명", max_length=50)

    def __str__(self):
        return self.category_name

# 블로그 게시글 모델
class Article(models.Model):
    author = models.ForeignKey(User, verbose_name="글 작성자", on_delete=models.CASCADE)
    title = models.CharField("글 제목", max_length=50)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    content = models.TextField("글 내용")

    def __str__(self):
        return f"{self.author.username}의 {self.title}입니다."
    