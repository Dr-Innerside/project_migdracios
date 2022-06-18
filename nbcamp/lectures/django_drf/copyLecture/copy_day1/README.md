# Django Rest Framework day1

## 📌 1일차 강의 목표
- Pycharm의 패키지 관리, Django 실행, 코드 스니펫 등에 의존하지 않고 프로젝트를 직접 구현 및 실행할 수 있어야 함
    - 편집기에서 제공해주는 기능들은 개발 속도를 향상시키기 위한 목적일 뿐, 너무 의존해서는 안됨
- DRF를 활용해 미니프로젝트를 구축할 수 있어야 함

## 🙋‍♂️ Django Rest Framework란?
- Django의 확장판. 기존 django에서 확장된 기능을 이용할 수 있음
- 대표적으로 Serializer를 사용하면, 같은 기능을 구현하는데 있어서 기존 django에서보다 예쁘고, 편해지고, 가독성이 좋아지는 등의 효과를 볼 수 있음

## ⚠ 프론트엔드와 백엔드를 구분한다?!
- 프론트엔드를 최대한 배제하고, 백엔드 위주로만 진행할 것!
- 그것을 위해 사용할 프로그램 POSTMAN
- UI 작업은 django admin 정도

---

## 🚩 DRF를 사용하기 위한 준비
### 1. drf 설치하기 
```
pip install django
pip install djangorestframework
```

### 2. settings.py 설정
INSTALLED_APPS에 'rest_framework' 추가하기
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : [ # 기본적인 view 접근 권한 지정
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [ # session 혹은 token을 인증 할 클래스 설정
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],
    'DEFAULT_PARSER_CLASSES': [ # request.data 속성에 액세스 할 때 사용되는 파서
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ]
}
```

## 🚩 기초 Python 문법
### def, 함수에 대한 이해
함수 기본 형태
```python
def test():
    pass
    return True
test()
```

### class, 클래스에 대한 활용 및 상속에 대한 이해
클래스 기본 형태
```python
class Test():
    def test(self):
        pass
        return True
```

클래스 상속이란?
- django를 하면서 많이 다룰 개념
- 직접 구현하는 정도는 필요하지 않을 것
- 부모 클래스, 자식 클래스가 존재하는데 자식 클래스에서 부모 클래스의 내용을 받아서 사용한다!

### 자료형(int, str, list, dict ...)
### list, iterator의 반복문에 대한 이해
### mutable과 immutable의 차이
```python
immutable = "String is immutable!"
mutable = ["list is mutable!"]

string = immutable
list_ = mutable

string += "immutable string!"
list_.append("mutable list!")

print(immutable)
print(mutable)
print(string)
print(list_)

# 해당 코드를 실행했을 때 나오는 결과를 유추하고
# mutable 자료형과 immutable 자료형은 어떤 게 있는지 알아야 함
```
mutable 객체는 다른 변수에 값을 할당할 때 | 주소 값을 넣는다
- mutable 변수와 list_ 변수는 같은 주소를 바라보고 있다
immutable 객체는 다른 변수에 값을 할당할 때 | 값을 넣는다

### deepcopy()
mutable 객체도 주소값을 바라보지 않고, 값을 할당할 수 있게 해줌
django 기본 라이브러리에 있기 때문에 바로 사용할 수 있음
```python
mutable = ["list is mutable!"]
list_ = deepcopy(mutable)
# list_ = mutable[:] 이것도 같은 값을 줌
list_.append("mutable list!")
```
### kwargs, args의 이해
```python
def test(num1, num2, *args, **kwargs):
# def test(num1, num2):
    print(f"num1: {num1}")
    print(f"num2: {num2}")
    print(args)
    print(kwargs)
    return 

# test(1, 2)
# test(1, 2, 3) # 오류가 발생함
test(1,2,
        3,4,5,6,7,8,
        num3=5, num4=2)
```
args(arguments)
- 함수에서 정해진 인자 값 이상의 값을 필요로 할 때마다 함수 식을 수정해 주는 것은 불편하다
- 명시할 변수 이외의 것을 args로 자유롭게 모두 받을 수 있다

kwargs(keyword arguements)
- args에 키워드가 붙음
- 딕셔너리 형태로 들어감

---

```python
def test(*args, ** kwargs):
    print(args)
    return True

sample_list = [1,2,3,4,5]
sample_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5",
}
test(*sample_list)
```

⚠ *args, **kwargs?
```python
a = [1,2,3,4,5]
print(a) # == print([1,2,3,4,5])
print(*a) # == print(1,2,3,4,5)
```
* 애스터리스크(asterisk) 한 개를 써주면 리스트 형식이 풀려서 값이 입력된다
- 따라서 위의 예제에서 함수(*인자값) 형태로 사용하면, 함수 안에서 값이 리스트가 풀려서 들어간다
** 애스터리스크 두 개를 써주면 딕셔너리 형식이 풀려서 값이 입력된다

🤔 args, kwargs를 사용하지 않은 기본 예제
```python
from user.models import User

def user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        gender = request.POST.get('gender')
        birthday = request.POST.get('birthday')

        user = User.objects.create(
            username=username,
            fullname=fullname,
            gender=gender,
            birthday=birthday
        )
```

😈 *args, **kwargs를 사용한 예제
```python
... 생략

def user(request):
    if request.method == "POST":
        user = User.objects.create(
            **request.POST
        )

```

### db에서 사용되는 CRUD와 django orm의 이해

### module을 import하는 구조에 대한 이해

### fstring에 대한 이해

### try, exception을 활용한 에러 처리

### stacktrace에 대한 이해
stacktrace를 가장 많이 볼 수 있는 곳은 실행 콘솔 창!
```python
def run_a():
    print(f"{a}함수가 실행되었습니다")
    run_b()
    return 
def run_b():
    print(f"{b}함수가 실행되었습니다")
    run_c()
    return 
def run_c():
    print(f"{c}함수가 실행되었습니다")
    run_d()
    return 
def run_d():
    print(f"{d}함수가 실행되었습니다")
    run_e()
    return 
def run_e():
    print(f"{e}함수가 실행되었습니다")
    raise Exception("에러 발생!!")
    return 

run_a()
```
🙋‍♂️ stacktrace?
- 위 함수의 경우 run_a() 함수를 실행하면 b를 타고, c를 타고, d를 타고, e를 타게 된다.
- 그 와중에 e를 통과하다가 에러발생!! 이라는 문구를 실행 콘솔에 출력하게 된다.
- 에러 실행 콘솔에는 단순히 에러가 발생한 e 뿐만 아니라, e를 포함하고 있게 되는 a/b/c/d 모두를 출력하게 된다.
- django 프로젝트 내부에서 작성한 다양한 python 파일들의 상위구조에 있는 프로젝트 파일들이 stacktrace에 의해 콘솔에 출력되니 참조할 수 있게 된다.


## 🚩 협업을 위한 Python 활용법
### 파이썬 가상환경 venv
```
# python terminal
python -m venv venv # 가상환경 생성
venv/Scripts/activate # 가상환경 진입
```

### requirements.txt
패키지를 관리하기 위한 파일
```
# python terminal
pip install django                  # 장고 설치
pip install djangorestframework     # drf 설치
pip freeze > requirements.txt       # requirements.txt에 설치한 pip list 에 작성
pip install -r requirements.txt     # requirements.txt에 기입된 pip install
```

### 코드 컨벤션
협업 시 코드를 짤 때 규칙을 지켜서 작성하겠다고 하는 약속
- 지키지 않았을 시, 서류 탈락할 가능성이 높음..
- 나중에 생산성과 관리를 위해서 작성함
    - class LogINUSERView 이런 식으로 작성한다면, 다른 팀원들이 못알아먹을 확률 높은
    - class A 이런 식으로 작성한다면, 어떤 클래스인지 다른 팀원들이 짐작하기 힘듦

파이썬에서의 코드 컨벤션은 Pascal, Snake 두 종류로 구분된다.
1. Pascal : UserLoginView
- class 만들 때 사용
2. Snake : user_login_view
- class 이외의 모든 경우에서 사용

코드 컨벤션을 지켜서 작성하면 어떤 것이 클래스, 일반 변수나 함수를 구분할 수 있게 된다.

3. 모두 대문자 : PIE = 3.14
- 상수에서 사용, 절대 바뀌지 않을 값이기에 대문자로 표현
4. 단수, 복수 명사
- 한 개는 단수여야 하고, 두 개 이상은 복수여야 한다
- user = "user1"
- user_list = ["user1", "user2", "user3"]
- users = ["user1"] -> 한 개의 값만 들어있지만 리스트 형태이기 때문에!
    - users = User.objects.all() 한 개일 수도, 두 개일 수도, 여러 개일 수도 있지만 
    - 여러 개를 조회하므로, 반복문을 사용하므로 복수 개를 처리하기 위한 목적이 있다는 것에 의의가 있음

### Http Status Code 에 대한 이해 
1. 2xx : normal
2. 3xx : redirect
- http://naver.com -> https://naver.com 으로 리다이렉션
3. 4xx : client error
- 404 not found
4. 5xx : server error

### 기본적인 터미널 활용
리눅스 및 터미널과 같은 CLI(Command Line Interface) 환경이 매우 많으므로 사용에 익숙해져야함
