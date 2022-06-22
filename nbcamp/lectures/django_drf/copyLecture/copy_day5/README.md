# Django Rest Framework day4

## 📌 5회차 강의 목표
- status code를 이해하고, 프로젝트에 적용할 수 있다.

## 🚩 Status Code
### 🤔 Status Code를 지정해 주지 않은 경우?
Status Code를 지정해주지 않는다면, 기본으로 200을 가리킨다.
- 기본으로 되어 있다고 하더라도 지정하는 편이 좋다!
    - 왜냐하면?

### Status Code를 지정하는 방법
1. status 임포트
2. return에 코드 넘버 작성
    - return Response({}, status=...) 의 형식으로 작성한다

Status Code 사용예시
```python
from rest_framework import status

class UserView(APIView):
    def get(self, request):
        # some error
        return ResPonse({"error": "some error message"}, status=status.HTTP_400_BAD_REQUEST)
        return ResPonse({"error": "some error message"}, status=400)
        return Response({"msg": "login success!"}, status=status.HTTP_200
        )
```

## ✍ settings.py 에 자주 사용하는 설정
### 🕵️‍♀️ SQL 디버깅 로그
ORM에 접근할 때 마다 어떤 쿼리가 작성되었는지 보여주고, 그 속도 또한 표시된다.
    - 이를 통해서 어느 부분에서 메모리 이슈가 있는지, 프로그램이 느려지는지 확인할 수 있다!
```python
# https://docs.djangoproject.com/en/1.11/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
```

## 🚩 커스텀 유저 모델 admin
커스텀으로 유저 모델을 생성하고, admin.py에 모델을 등록한 뒤 관리자 페이지에서 레코드를 관리할 때, 사용자 비밀번호가 해싱되지 않고 평문으로 작성되어 사용할 수 없는 현상이 발생한다.

이를 해결하기 위해 UserAdmin 설정을 해주어야 한다!

```python 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'fullname', 'email')
    list_display_links = ('username', )
    list_filter = ('username', )
    search_fields = ('username', 'email', )

    fieldsets = (
        ("info", {'fields': ('username', 'password', 'email', 'fullname', 'join_date', )}),
        ('Permissions', {'fields': ('is_admin', 'is_active', )}),
    )

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date', )
        else:
            return ('join_date', )

admin.site.register(UserModel, UserAdmin)
```

1. UserAdmin as BaseUserAdmin 임포트
    - 기존 UserAdmin을 BaseUserAdmin으로 변경한다. 
    - 상속하기 위한 클래스이므로 Base를 붙여주어 가독성을 높이는 듯 하다
2. class UserAdmin 생성
    - 이름은 자유롭게 지정가능함
3. register에 등록
    - 생성한 클래스를 admin.site.register에 사용할 모델과 같이 등록


## 🔥 Permission class 심화
### 📜 admin은 모두 가능하고, 로그인 사용자는 조회만 가능한 Permission
커스텀 퍼미션을 통해서 사용자가 어디부터 어디까지 접근할 수 있는지 상세하게 조작할 수 있다.

아래의 경우는 관리자 계정인 경우 모든 것에 접근이 가능하지만, 로그인한 사용자는 조회만 가능하도록 설정한다!

```python
from rest_framework.exceptions import APIException

class IsAdminOrIsAuthenticatedReadOnly(BasePermission):
    """
    admin 사용자는 모두 가능, 로그인 사용자는 조회만 가능
    """
    SAFE_METHODS = ('GET', )
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response ={
                    "detail": "서비스를 이용하기 위해 로그인 해주세요.",
                }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if user.is_authenticated and user.is_admin:
            return True
            
        if user.is_authenticated and request.method in self.SAFE_METHODS:
            return True
        
        return False
```
참고사항
1. SAFE_METHOD를 통해서 특정 HTTP METHOD 마다 다른 권한을 설정할 수 있다!
    - 조회, 생성을 가능하게 한다면 ```('GET', 'POST', )``` 처럼 작성하면 된다
2. 관리자/로그인 계정 이외의 제 3의 분기인 비로그인 사용자에 대한 GenericAPIException
    - 관리자 계정도, 로그인한 계정도 아닌 분기가 존재한다. 바로 로그인 하지 않은 사용자!
    - 로그인 하지 않은 사용자는 아예 권한이 없는 경우이므로 아예 타는 분기가 다르다!
    - class GenericAPIException을 생성하고, 로그인 조회 후 비로그인이라면 exception으로 보내버린다
    - 커스텀 퍼미션 내부의 접근 권한 없음 메시지는 관리자 이외의 로그인한 유저 중 권한이 없는 부분에 대한 알림 메시지이다!
3. views.py 에 퍼미션을 임포팅하고 POSTMAN으로 테스트해보자
    - is_admin에 체크되어 있지 않은 유저(admin페이지에서 확인 가능)는 메시지와 함께POST 접근이 거부된다.
        - detail : 접근 권한이 없습니다.
    - 로그인 하지 않은 사용자는 메시지와 함께 API 접근 자체가 거부된다.
        - detail : 서비스를 이용하기 위해 로그인 해주세요
    - admin 계정은 모든 권한에 제대로 접근한다!

## 🔥 django admin 심화

```python
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'fullname', 'email')
    list_display_links = ('username', )
    list_filter = ('username', )
    search_fields = ('username', 'email', )

    fieldsets = (
        ("info", {'fields': ('username', 'password', 'email', 'fullname', 'join_date', )}),
        ('Permissions', {'fields': ('is_admin', 'is_active', )}),
    )

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date', )
        else:
            return ('join_date', )
```

### list_display
    - admin에서 테이블 형식으로 보여줄 필드
### list_display_link
    - 클릭 시 상세 페이지로 들어갈 수 있는 필드
### list_filter
    - filter를 적용할 수 있는 필드
### search_fields
    - 검색창이 생기고, 검색 받을 항목 필드
### fieldsets
    - 상세 페이지를 더 깔끔하게 볼 수 있음
### readonly_fields
    - 수정할 수 없지만 볼 수 있게 만들 필드
    - 작성할 때는 적을 수 있고, 수정은 불가능하게 하려면?
        - 변수가 아닌 함수 get_readonly_fields로 작성해야 한다!

### tabularinline / stackline
    - 역참조관계에서만 가능한 어드민에서 역참조 모델도 같이 보여줌
    - tabularline은 세로, stackline은 가로로 보여줌
        
### filter_horizontal
    - 필드를 넣어 