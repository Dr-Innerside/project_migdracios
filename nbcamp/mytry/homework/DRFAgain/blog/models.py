from django.db import models
from django.forms import CharField

from user.models import User as UserModel

from django.utils import timezone


# Create your models here.


    
# 2번과제. 외래 키를 사용해서 Article, User 테이블과 관계를 맺어주세요

# 2일차 5번과제. blog/models.py에 <카테고리 이름, 설명>이 들어갈 수 있는 `Category`라는 모델을 만들어보세요.
class Category(models.Model):
    name = models.CharField("카테고리 이름", max_length=50)
    desc = models.CharField("카테고리 설명", max_length=50)
    
    def __str__(self):
        return self.name
    
# 2일차 6번과제. blog/models.py에 <글 작성자, 글 제목, 카테고리, 글 내용>이 들어갈 수 있는 `Article` 이라는 모델을 만들어보세요.
# (카테고리는 2개 이상 선택할 수 있어야 해요)

class Article(models.Model):
    author = models.ForeignKey('user.User', verbose_name="글 작성자", on_delete=models.CASCADE)
    title = models.CharField("글 제목", max_length=50)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    content = models.TextField("글 내용")
    exposure_start_date = models.DateField("게시 시작 일자", default=timezone.now)
    exposure_end_date = models.DateField("게시 종료 일자", default=timezone.now)
    
    def __str__(self):
        return f"{self.author} 님의 {self.title}"
    
# 3일차 1번과제. blog 앱에 <게시글, 사용자, 내용>이 포함된 comment 테이블을 작성해주세요
class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name="게시글", on_delete=models.CASCADE)
    author = models.ForeignKey('user.User', verbose_name="글 작성자", on_delete=models.CASCADE)
    content = models.TextField("내용")
    
    def __str__(self):
        return f"#{self.author.username}#이(가) 작성한 @{self.article.content}@의 댓글입니다."
