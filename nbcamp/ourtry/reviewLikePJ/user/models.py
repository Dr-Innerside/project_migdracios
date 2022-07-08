from django.db import models
from django.forms import CharField

# Create your models here.
class Like(models.Model):
    like = models.CharField("좋아용", max_length=50)

class User(models.Model):
    username = models.CharField("아이디", max_length=50)
    password = models.CharField("비밀번호", max_length=50)
    like = models.ManyToManyField(to=Like ,verbose_name="좋아요")
    
    def __str__(self):
        return self.username