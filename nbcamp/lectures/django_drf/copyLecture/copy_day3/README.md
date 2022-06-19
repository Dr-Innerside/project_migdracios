# Django Rest Framework day3

## 📌 3일차 강의 목표
- Rest API에 대한 이해
- views.py에서 리퀘스트 처리하기
- POSTMAN을 활용한 리퀘스트 실습
- DB ORM과 구조에 대한 이해

## 🚩 REST API에 대한 이해
http method의 종류

```python
if request.method == 'GET':
    # 조회
if request.method == 'GET':
    # 생성
```

1. get : 조회
2. post : 생성
3. put : 수정
4. delete : 삭제

## 🤹‍♀️ FBV, CBV?
django에서 views.py를 통해 API를 구현할 때, 작성할 수 있는 방법을 의미한다.
각각 함수 기반, 클래스 기반을 의미한다.

### 🗨 Function Base View
함수로 view를 생성

### 🗨 Class Base View
클래스로 view를 생성
- 일반적으로 많이 쓰임

```python
# Class Base View
class UserView():
def get(self, request):
    # 사용자 정보 조회
    pass    
def post(self, request):
    # 회원가입
    pass
def put(self, request):
    # 회원 정보 수정
    pass
def delete(self, request):
    # 회원 탈퇴
    pass

# Function Base View
def user_view(request):
    if request.method == 'GET':
        pass
```
#### ⚠ CBV 리퀘스트 함수 이름은 고정?!
CBV 방식으로 작성할 때는 받아올 http method인 get, post, put, delete라고 함수 이름을 고정시켜 주어야 인식한다.
- 그것이 DRF에서 지정한 약속이기에.

#### 🤹‍♀️ 그럼 method 안에 함수를 써주고 싶다면?
CBV 밖에서 함수를 하나 새로 생성해서 안에서 호출하는 방식을 사용하기

```python
...생략
def sum_(num1, num2):
    return num1+num2

class UserView(APIView):
    ...
    def get(self, request):
        sum_(**request.data)
        return Response({"msg": "get method!!"})
    ...
```

### 🔥 Permission Class?
- Class Base View를 사용할 때, Django Rest Framework에서 지원하는 기능.
- 작성하고 있는 CBV의 권한을 지정해 줄 수 있음
- 사용자가 접근할 때, 누구나 조회/로그인 한 유저만 조회/관리자 계정만 조회 등
- Permission Class를 활용하여 가입일 기준 1주일 이상 지난 사용자만 접근하는 등의 적용가능

1. import APIView
- Permission Class를 사용하기 위한 라이브러리
2. APIView를 상속
- 작성한 CBV에 APIView를 상속시켜 APIView의 기능을 사용할 수 있게 함
3. import permissions
- APIView를 상속받은 상태에서 권한 설정을 추가로 걸어줄 라이브러리 permissions 임포트
4. permission_classes 변수에 권한 주기
- permissions.AllowAny는 모두에게 허용하는 권한을 설정한 것이다!


```python
from rest_framework.views import APIView
from rest_framework import permissions

class UserView(APIView):
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAdminUser]
    ... 생략
```

#### 🤔 오타가 나도 제대로 작동한다?
- permission의 기본값은 AllowAny이기 때문에, AllowAny로 세팅했는데 오타가 있었다면 작동했을 것이다!
- 마찬가지로 rest_framework settings.py 셋업도 해야하지만, 이것도 없으면 기본 값인 AllowAny를 사용하도록 되어있다!

### 🔥 return Response?
기존방식은 render, redirect를 사용했었으나 DRF에서는 Response를 활용하여 API를 처리할 것

1. import Response
2. Response 방식 
```python
# render
return render(request, 'index.html')

# redirect
return redirect('/home')

# Response
from rest_framework.response import Response

return Response({"msg": "GET method!"})
```

## 🚩 POSTMAN 활용
프론트엔드 UI가 존재하지 않을 때 view를 테스트하기 위해서 필요한 프로그램

1. 워크스페이스를 만들어 팀원과 공유하자!
- 워크스페이스를 만들어 팀원과 만들어 둔 테스트 형태를 모두 반복적으로 작성할 필요없이 이용할 수 있으며, 또한 수정도 가능하기에 협업에 용이
2. 새로운 request를 만들어 주소와 http method를 입력하고 send를 해서 테스트해보기

### 📜 POSTMAN에 데이터를 담아서 백엔드로 보내기
1. Collection -> 원하는 Request -> Body -> raw
- 보내줄 데이터 형식은 JSON으로 변경해주기!
- JSON은 dict와 같게 작성해주면 됨(""큰 따옴표로 작성해야 한다!)
2. 백엔드 request.data에서 해당 값을 받아서 처리!

```
# POSTMAN-body-raw
{
    "num1" : 5,
    "num2" : 10
}
```

```python
def get(self, request):
    print(request.data) # JSON 형식의 데이터
    result = sum_(**request.data) # request.data 언패킹
    Response({"msg": f"get method -- sum result->{result}})
```
#### 🔥 언패킹 응용! kwargs가 아닌, args를 POSTMAN에서 JSON으로 보낸다면?
```python
# 응용! *args 로 언패킹해서 데이터 사용하기
# postman
{
    "numbers": [1,2,3,4,5,6]
}
# def sum
sum_(*args):
    return sum(args)
# def get
numbers = request.data.get("numbers",[])
result = sum_(*numbers)
```

### ⚠ POST/PUT/DELETE 통신 시 csrf error가 발생할 때?!
django에서 csrf로 데이터 유효성 검사를 실행하듯이 DRF에서도 사용해줘야 한다.
POSTMAN에서 아래의 코드를 함께 작성해야 한다!

```
var xsrfCookie = postman.getResponseCookie("csrftoken");
postman.setGlobalVariable('csrftoken', xsrfCookie.value);
```
또한 헤더에 담아서 보내줘야 한다
- KEY : X-CSRFToken
- VALUE : {{ csrftoken }}
- test에서 적은 것보다 정석은, 하단부 Cookies에서 csrftoken의 value를 복사해서 헤더 value에 붙여넣어 send!
- 이를 자동화 한것이 test 스크립트

## 🚩 DB ORM과 구조에 대한 이해

### queryset, object의 차이에 대한 이해
1. queryset
- 쿼리셋은 오브젝트의 집합
```python
users = User.objects.filter(id=id) # return queryset
# queryset : [obj1, obj2, obj3]
# objects.filter는 오브젝트 개수와는 큰 관련이 없다
```
2. object
- 오브젝트는 단일 오브젝트
```python
user = User.objects.get(id=id) # return object
# objects.get은 반드시 하나의 오브젝트 만을 필요로 한다. 없거나, 두 개 이상일 경우 에러!
```
### ✍ ORM으로 데이터 추가,조회,수정,삭제하기
```python
# 추가1
model = Model(
    field1="value1",
    field2="value2"
)
model.save()

# 추가2
Model.objects.create(
    field1="value1",
    field2="value2"
)

# 조회
Model.objects.all()
Model.objects.filter()
Model.objects.get()

# 수정1
model = Model.objects.get(id=obj_id)
model.field = value
model.save()

# 수정2
Model.objects.filter(field__contains=value).update(
    field1="value1",
    field2="value2"
)

# 삭제
Model.objects.filter(field="value").delete()
Model.objects.get(id=obj_id).delete()
```

🤹‍♀️ 수정2에서 field__contains=value, double underbar?
- 추가 예정. LINK--

### 🔥 자주 사용하는 패턴 코드
1. objects.get() 이 없을 때 사용하는 이벤트
```python
try:
    Model.objects.get(id=obj_id)
except Model.DoesNotExist:
    # some event
    return Response("존재하지 않는 오브젝트 입니다.")
```
2. order_by()를 사용하여 가입일을 조회
```python
Model.objects.all().order_by("join_date")

# 추가
# -join_date를 붙이면 역순으로 정렬
# .order_by("?") 사용 시 무작위 셔플
```
3. 첫번 째 쿼리셋을 가져오는 메서드 .first()
```python
Model.objects.all().first()
# all()[0] 과 동일한 메서드
```
4. get_or_create()
- 입력한 object가 존재할 경우 해당 object를 가져오고,
- 존재하지 않을 경우 새로 생성함
```python
model, created = Model.objects.get_or_create(
    field1="value1",
    field2="value2"
)
if created:
    # created event
else:
    # already exist event
```

## 🎯 DRF Custom UserModel 생성 및 사용자 로그인 구현
실제 실무에서는 django에서 기본으로 제공하는 AbstractUser가 아닌, DRF 커스텀 사용자 모델을 사용하여 개발한다.
- custom user model은 생성 시 필드 들을 자유롭게 커스텀 할 수 있기 때문!
- custom user model을 만들기 위해 필요한 설정은 외우지 않고 가져다 쓰기!

1. import BaseUserManager, AbstractBaseUser
- 커스텀 모델을 사용하기 위한 라이브러리
2. AbstarctBaseUser 상속
- 커스텀 유저 모델을 받기 위해 상속하는 클래스
3. 필드 생성
- 아이디, 비밀번호, 이메일, 가입일 등을 모델 필드에 추가한다.
4. settings.py에 AUTH_USER_MODEL = 'user.User' 세팅
- global settings.py를 참조하면 기본 AUTH_USER_MODEL = 'auth.model' 로 되어있다.
- 내가 사용할 커스텀 모델의 유저 모델이라는 것을 설정해 주어야 작동한다.
5. USERNAME_FIELD = 'username'
- 웹마다 아이디/패스워드, 이메일/패스워드를 다르게 입력받는 곳이 있다.
- 그래서 뭘 아이디로 받을 건데? 에 해당하는 설정이다.
- 위의 경우 username, 즉 테이블에서 사용자 계정을 아이디로 받겠다는 것이다.
- 이메일을 아이디로 받고 싶을 때는, USERNAME_FIELD = 'email' 이렇게 하면 된다!
6. REQUIRED_FIELD = []
- 딱히 사용할 일은 없음
- createsuperuser를 대표적으로 사용하게 될 여러 기능들을 작동하게 해줄 설정
- 설정할 때 값을 email, fullname 등을 적어준다면, createsuperuser 등의 기능을 작동할 때 입력 받게 된다.
7. is_active, is_admin 설정
- 활성화 계정인지, 관리자 계정인지 설정하는 값
8. 가독성을 위한 str(self) 함수
- 오브젝트를 생성하면 object(1) 이런 식으로 조회하게 되는데,
- 이를 str함수의 리턴 값을 지정해주어 보기 쉽게 할 수 있다.
```python
def __str__(self):
    return fullname
# 이렇게 작성해두면, 사용자가 계정을 생성할 때 오브젝트의 이름을 object(1) 대신, 김철수 로 받게 된다.
```
9. has_perm, has_module_perm 설정
- 테이블의 권한을 설정
- 관리자 계정이라면 권한을 주고, 아니라면 안주고.
- admin일 경우 무조건 True, 비활성 사용자(is_active=False)의 경우 항상 False
- 기본 세팅 이후 손대지 않음
10. is_staff 설정
11. UserManager 지정
- 모델에 objects = UserManager() 추가
- 사용자 계정, superuser 계정 생성 함수를 만들어서 실제 생성시 함수를 타고 실행됨

### ⚠ migration 에러 발생시에는 새출발하기
- 작성한 앱의 migrations 폴더의 0001~과 같은 마이그레이션 파일을 지운다.
- db.sqlite3 파일을 삭제한다.
- makemigrations, migrate 커맨드를 다시 입력!

### 🔥 Custom User Model을 활용하여 로그인하기!
1. Permissions 확인!
- AllowAny는 모든 사용자, IsAuthenticated는 로그인한 사용자! 확인해보고 로그인 뷰 만들기
2. UserAPIView 생성
- UserView는 IsAuthenticated로 변경한 뒤, AllowAny로 적용되는 새로운 CBV 생성
3. import login, authenticate
- django.contrib.auth에서 가져온다

#### ✍ API에 주석달기
- 가독성을 위해서!
- 조금 더 자세하게 작성하려면 Docstring 을 활용해보자!
```python
# 한줄 주석
def get():
    '''
    Docstring:
    로그인 한 사용자의 정보를 데이터에 포함시켜서 리턴
    '''
```

### 🎢 Custom User Model을 활용하여 로그아웃하기!
1. http method DELETE!
2. contrib.auth import logout
3. logout(request)

```python
def delete(self, request):
    logout(request)
    return Response({"message": "delete method!"})
```