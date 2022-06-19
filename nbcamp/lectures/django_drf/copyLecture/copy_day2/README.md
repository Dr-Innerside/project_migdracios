# Django Rest Framework day2

## 📌 2일차 강의 목표
- 데이터베이스 용어 정리
- django 프로젝트 구조에 대한 이해

## 🚩 데이터베이스 용어 정리
1. RDBMS(RDB, Relational Database Management System)
- 관계형 데이터베이스 관리 시스템, MySql, OracleDB 등 관계형 데이터베이스를 지칭한다.
2. Sql(Structured Query Language)
- select, insert 등과 같은 데이터베이스 쿼리를 날려 데이터베이스의 CRUD를 위해 사용됨
3. NoSql(Not Only Sql)
- 관계형 데이터베이스가 아닌 다른 형태로 데이터를 저장하며, mongoDB가 이에 해당
- 관계형 데이터베이스 만큼 유효성을 지켜주지는 않음
- 대용량의 데이터를 넣고 가져오는데 유리함
4. Table
- DB는 기본적으로 테이블로 이루어져 있으며, 필드와 레코드(django에서는 object)가 존재한다.

```python
# models.py
class User(models.Model):
    username = models.CharField("사용자 계정", max_length=50)
    password = models.CharField("비밀번호", max_length=50)

    # User라는 테이블에 username, password라는 필드가 존재함
    # 사용자가 회원가입을 할 때마다 레코드가 하나씩 추가됨.
    # 즉, 레코드란 데이터베이스에 저장 되는 값들을 지칭하는 것
```

5. key
- FK : Foreign Key의 약자이며, 다른 테이블을 참조 할 때 사용된다.
- UK : Unique Key의 약자이며, 중복 값을 허용하지 않는다.
    - 회원가입할 때, 사용자 계정이 대표적인 UK
- PK : Primary Key의 약자이며, 테이블에서 반드시 존재해야 한다.
    - 한 테이블에 두 개 이상 존재할 수 없음
    - UK의 상위개념
    - FK를 사용할 경우 참조 할 테이블의 PK를 바라본다.
    - 테이블을 추가하고 migration 파일을 찾아보면 id값이 바로 PK인데,
    - models.py로 지정해주지 않으면 자동으로 생성된다.

```python
username = models.CharField("사용자 계정", max_length=50, unique_key=True)
# UK는 여러 개 일 수는 있다! 다만 이것은 다른 레코드 값들과는 다른 특별한 값
password = models.CharField("비밀번호", max_length=50, primary_key=True)
# PK는 두 개 있다면 바로 오류를 내뱉는다! 없어도, 두 개 이상이어도 안되는 값
```

## 🚩 django 프로젝트 구조에 대한 이해
1. settings.py
- django 프로젝트를 실행할 때 해당 파일을 참조한다
- 데이터베이스 설정, 앱 설정, 기본 정책 설정등을 할 수 있다.
2. models.py
- DB에 테이블을 추가하고 관리할 때 사용된다.
- 테이블에 들어갈 필드, 필드의 속성 값 등을 설정할 수 있다.
- python manage.py makemigrations/migrate 명령어를 통해 설정을 DB에 반영시킬 수 있다.
3. views.py
- django에서 request 데이터를 받은 후 처리할 전반적인 로직이 들어간다.
- urls.py에서 views에 있는 class나 함수를 호출해서 사용하게 된다.
4. urls.py
- 웹에서 django 프로젝트로 request를 전달할 때 받아줄 경로를 설정할 수 있다.

## 🤹‍♀️ DB 모델링 실습
```python
#  models.py
from django.db import models

# 사용자 모델 : 기본적인 사용자 정보
class User(models.Model):
    username = models.CharField("사용자 계정", max_length=20, unique=True)
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=60)
    fullname = models.CharField("이름", max_length=20)
    join_date = models.DateTimeField("가입일", auto_now_add=True)

# 사용자 프로필 모델 : 사용자 상세 정보
class UserProfile(models.Model):
    # 사용자를 One-to-One 으로 바라봄
    user = models.OneToOneField(to=User, verbose_name="사용자", on_delete=models.CASCADE)
    # 사용자를 Many-to-Many 로 바라봄
    hobby = models.ManyToManyField(to="Hobby", verbose_name="취미")
    introduction = models.TextField("소개")
    birthday = models.DateField("생일")
    age = models.IntegerField("나이")

# 취미 모델
class Hobby(models.Model):
    name = models.CharField("취미", max_length=50)
```

### 🔥 FK에서 사용되는 on_delete 속성에 대하여
위 코드를 예시로 사용자모델을 참조하는 사용자 프로필의 유저와,
취미모델을 참조하는 사용자 프로필의 취미는 각각 사용자모델과, 취미모델의 레코드가 삭제된다면 어떻게 되는 것인가?

1. CASCADE : FK로 참조하는 레코드가 삭제 될 경우 해당 레코드를 삭제한다.
2. SET_NULL : FK 필드의 값을 Null로 변경해준다. null=True가 정의되어 있어야 사용 가능하다.
3. PROTECT : 해당 레코드가 삭제되지 않도록 보호해준다.
4. SET_DEFAULT : FK 필드의 값을 default로 변경해준다. default=""가 정의되어 있어야 사용 가능하다.
5. SET() : FK 필드의 값을 SET에 설정된 함수를 통해 원하는 값으로 변경할 수 있다.
6. DO_NOTHING : 아무런 동작을 하지 않는다. 참조 관계의 무결성이 손상될 수 있기 때문에 권장하지 않는다.

### ⚠ DateField와 DateTimeField는 다르다?!
DateField와 DateTimeField는 default 값을 여러 형태로 지정할 수 있다.

1. default = $date : 지정한 값을 기본 값으로 설정한다.
2. auto_now_add = True : 레코드가 생성될 때의 date를 기준으로 값을 지정한다.
3. auto_now = True : 레코드가 save() 될 때마다 갱신된다.

❌ 위의 값을 두 개 이상 같이 쓸 수 없다!

## admin 페이지 활용
모델링 한 테이블들을 admin에서 추가, 확인, 수정하기

```python
# admin.py
from django.contrib import admin
from user.models import User, UserProfile, Hobby

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Hobby)
```

admin 커스텀은 심화과정에서--LINK(차후 추가)