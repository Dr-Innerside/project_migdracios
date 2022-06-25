from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# 2. user/models.py에 `Custom user model`을 생성한 후 django에서 user table을 생성 한 모델로 사용할 수 있도록 설정해주세요
class User(AbstractBaseUser): 
    username = models.CharField("아이디", max_length=50, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    email = models.EmailField("이메일", max_length=254)
    fullname = models.CharField("실명", max_length=50)
    join_date = models.DateTimeField("가입일", auto_now_add=True)
    
    		# is_active가 False일 경우 계정이 비활성화됨
    is_active = models.BooleanField(default=True) 

    # is_staff에서 해당 값 사용
    is_admin = models.BooleanField(default=False)
    
    # id로 사용 할 필드 지정.
    # 로그인 시 USERNAME_FIELD에 설정 된 필드와 password가 사용된다.
    USERNAME_FIELD = 'username'

    # user를 생성할 때 입력받은 필드 지정
    REQUIRED_FIELDS = []
    
    objects = UserManager() # custom user 생성 시 필요
    
    def __str__(self):
        return self.username

    # 로그인 사용자의 특정 테이블의 crud 권한을 설정, perm table의 crud 권한이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_perm(self, perm, obj=None):
        return True
    
    # 로그인 사용자의 특정 app에 접근 가능 여부를 설정, app_label에는 app 이름이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_module_perms(self, app_label): 
        return True
    
    # admin 권한 설정
    @property
    def is_staff(self): 
        return self.is_admin
    
class UserProfile(models.Model):
    user = models.OneToOneField(to="user.User", verbose_name="사용자 프로필", on_delete=models.CASCADE)
    bday = models.DateField("생일", default="")
    age = models.IntegerField("나이")
    hobby = "" # 일단 공란
    self_intro = models.TextField("자기소개")
    
    def __str__(self):
        return f"{self.user.username}의 프로필"
    
