from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

# 사용자 매니저
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# 사용자 모델
class User(AbstractBaseUser):
    username = models.CharField("아이디", max_length=50, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    email = models.EmailField("이메일", max_length=254)
    fullname = models.CharField("실명", max_length=50)
    join_date = models.DateTimeField("가입일", auto_now_add=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELD = []

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True


    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    objects= UserManager()

# 사용자 프로필
class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="사용자 프로필", on_delete=models.CASCADE)
    age = models.IntegerField("나이")
    introduction = models.TextField("자기소개")

    def __str__(self):
        return f"{self.user.username}의 프로필이지롱?!"
