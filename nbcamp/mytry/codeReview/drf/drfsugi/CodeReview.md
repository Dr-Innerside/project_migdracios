# nicesugi drf code copy

## ✍ 작성목적
- 작성된 코드를 읽고 작동원리를 이해한다.
- 작성된 코드를 바탕으로 내 프로젝트에 적용할 수 있다.
- 작성된 코드를 자신이 문서화 할 수 있다 또는 타인에게 설명할 수 있다

## 🕵️‍♀️ 어플리케이션 구조

### 💾 Django
DRF 프로젝트의 전체 설정 및 권한, url접근에 관한 내용이 작성되어 있다.
- 📌 settings.py 
    - djgnao, drf 프로젝트의 기본 설정과 관련된 내용이 있다. 
    - 언어/설치 어플리케이션/디버깅/각종 설정이 포함되어 있다.
    - INSTALLED_APPS에는 rest_framework, 설치할 앱 user/blog/product를 기입해주어야 어플리케이션을 인식한다.
    - REST_FRAMEWORK의 내용을 작성해주어 DRF 기본 세팅을 인식하게 한다.
    - LOGGING을 작성하여 디버깅 시 사용되는 쿼리와 메모리 속도를 파악할 수 있다.
    - AUTH_USER_MODEL을 작성하여 커스텀 사용자 모델 사용 시 적용할 수 있다.
- 📌 urls.py
    - 통합환경 및 POSTMAN과 같은 프로그램을 통하여 API에 접근할 때의 URL을 작성해주는 내용이 있음
    - path를 통해서 어떤 URL에 접근할 것인지 작성할 수 있다.
    - include를 통해서 다른 APP의 URL에 접근할 수 있게 한다.
        - path('주소', include('포함할 앱 이름.urls')) 의 형태로 작성한다.
- 📌 permissions.py
    - API에 접근할 때, 사용목적에 걸맞는 접근 권한을 설정할 Permission 클래스들을 작성해 놓는 파일
    - BasePermission을 가져와 사용목적에 맞게 커스텀 할 수 있다.



### 💾 user
user APP에서는 사용자의 정보와 관련된 기능이 작성되어 있다.
- 📌 admin.py
    - admin 페이지에서 user APP에서 작성 된 내용을 확인할 수 있도록 커스텀 하는 내용이 작성되어 있다.
        - admin 페이지에서 보여줄 model을 등록한다.
            - admin.site.register()가 해당
        - 커스텀 admin 페이지로 추가적으로 보여줄 내용을 작성한다.
            - class UserAdmin, UserProfileInline이 해당
- 📌 models.py
    - user APP에서 사용할 데이터베이스와 관련한 모델을 작성한다.
        - class User는 사용자 기본정보 모델에 해당한다.
        - class UserManager는 사용자 레코드 작성에 해당한다.
        - class Hobby는 사용자 취미 모델에 해당한다.
        - class UserProfile은 사용자 상세정보 모델에 해당한다.
- 📌 urls.py
    - 통합환경, POSTMAN 등에서 user APP에 접근할 URL을 작성한다.
    - urlpattens 리스트 안에 path()를 작성한다.
        - 'login/'과 같이 실제 접근할 url을 작성한다.
        - views.클래스(혹은 함수)를 작성하여 해당 url에 접근하면 작동할 클래스 및 함수를 선언한다.
        - 추가로 name을 작성하여 url을 특정할 수 있다.
    - user/로 시작하여 작성된 url을 추가하여 user/login/ 과 같이 접근하게 된다.
- 📌 views.py
    - user APP에서 사용될 API의 로직의 전반적인 부분이 작성되어 있다.
    - class UserView는 localhost:8000/user/ 로 접근하여 사용자 조회/회원가입/회원정보 수정/회원탈퇴 기능이 http Method get/post/put/delete로 구분하여 작성되어 있다.
    - class UserAPIView는 localhost:8000/user/login/ 으로 접근하여 로그인/로그아웃 기능이 http Method post/delete로 구분하여 작성되어 있다.
- 📌 serializers.py
    - user APP의 views에서 요청한 데이터베이스 레코드를 참조/역참조 및 정제하여 돌려주는 기능을 담당한다.
    - HobbySerializer는 사용자 모델 Hobby를 가져와 돌려줄 필드를 설정해 정제한다.
        - 취미를 선택한 사용자를 역참조하여 리턴할 필드에 추가되어 있다.
    - UserProfileSerializer는 사용자 모델 UserProfile을 가져와 돌려줄 필드를 설정해 정제한다.
        - HobbySerializer를 필드로 가져와 추가되어 있다.
        - serializer.ListField를 필드로 가져와 get_hobbys로 추가되어 있다.
    - UserSerializer는 사용자 모델 User를 가져와 돌려줄 필드를 설정해 정제한다.
        - UserProfileSerializer, ArticleSerializer를 가져와 필드에 추가되어 있다.
        - def validation이 작성되어 있다.
        - def create가 작성되어 있다.
        - def update가 작성되어 있다.
        - 사용되는 필드마다 적용할 옵션을 extra_kwargs에 지정되어 있다.
        

### 💾 blog
blog APP에서는 게시글 정보와 관련된 기능이 작성되어 있다.
- 📌 admin.py
    - 어드민 페이지에 등록할 테이블이 추가되어 있다.
    - admin.site.register(모델이름) 처럼 작성하여 Category, Article, Comment 모델을 어드민 페이지에 추가한다.
- 📌 models.py
    - 게시글과 관련된 데이터베이스 모델이 작성되어 있다.
    - class Category는 게시글 카테고리와 관련된 모델이다.
    - class Article은 게시글과 관련된 모델이다.
    - class Comment는 게시글 코멘트와 관련된 모델이다.
- 📌 urls.py
    - 게시글 관련된 view에 접근할 url이 작성되어 있다.
- 📌 views.py
    - 게시글과 관련된 API의 로직이 작성되어 있다.
    - class ArticleView는 게시글 조회/작성이 HTTP METHOD get/post로 나뉘어 작성되어 있다.
    - class CommentView는 코멘트 조회/작성이 HTTP METHOD get/post로 나뉘어 작성되어 있다.
- 📌 serializers.py
    - blog/views.py에 작성된 API에서 불러올 데이터를 정제하는 것이 작성되어 있다.
    - class CommentSerializer는 blog/models.py에 작성된 CommentModel을 참조하여 필드를 선정하여 데이터를 반환한다.
        - get_user 함수를 사용하여 코멘트를 작성한 사용자를 참조한다.
    - class ArticleSeirlaizer는 blog/models.py에 작성된 ArticleModel을 참조하여 데이터를 반환한다.
        - ManyToMany관계인 Category모델을 참조하여 필드에 추가되었다.
        - get_category 함수를 사용하여 카테고리를 선택한 게시글을 역참조하여 데이터를 반환한다.
        - extra_kwargs를 사용하여 각 필드에 해당하는 옵션을 지정한다.

### 💾 product

## 🎯 Django Project
### 💾permissions.py
#### 👨‍💻 **class RegistedMoreThanThreeDaysUser**
가입일 기준 3일 이상 지난 사용자만 접근 가능할 수 있게 하는 Permission
def has_permission을 통해 True를 반환하며, True일 때만 view의 API가 작동할 수 있게 한다.

##### 👨‍💻 가입3일 권한 def has_permission 
함수 has_permission에서의 로직은 다음과 같다.
    1. request.user로 사용자 정보를 변수 user에 초기화
    2. 사용자가 없거나, 로그인되어 있지 않는다면 False 반환
    3. request.user에 등록된 UserModel 중 DateTimeField인 가입일 join_date를 join_date 변수로 초기화
    4. 가입일에서 3일이 지났는지를 조회하기 위해 현재시간에서 3일을 뺀 날짜를 three_days_ago 변수에 초기화
        - 현재 날짜는 django.util 라이브러리의 timezone을 사용하여 timezone.now() 작성
        - 날짜 시각은 datetime 라이브러리의 timedelta를 사용하여 timedelta(days=3) 작성
    5. 가입일 join_date(예:01/05)가 현재에서 3일을 뺀 날짜(예: 01/04)보다 크다면(미래시점) 아직 3일을 채운 제 날짜가 아니기 때문에 권한 없음!
        - bool(join_date < three_days_ago) 형식으로 리턴하면 위의 조건대로라면 가입일이 제대로 맞춰지면 True를 아니라면 False를 반환하게 된다.
        - if/else 구문을 사용하여 분기를 거치는 것 보다 추가 작업 없이 True/False 반환이 가능하다!

#### 👨‍💻 **class IsAdminOrIsAuthenticatedReadOnly**
관리자 계정은 모든 접근을 허용하고, 가입한 사용자는 조회(열람, 읽기)만을 허용하는 Permission

    - 📌 SAFE_METHOD
        - SAFE_METHOD를 작성해주는 것으로 접근을 허용할 HTTP METHOD를 설정할 수 있다.
        - SAFE_METHOD = ('GET', ) 처럼 작성하여 로그인한 사용자는 GET, 조회만 가능하다!
    - 📌 message
        - message를 작성해주는 것으로 로그인한 사용자가 권한이 없는 HTTP METHOD에 접근할 때 사용자에게 접근을 허용하는 대신 알림을 보여줄 수 있다.
        - message = '접근 권한이 없습니다.' 와 같이 사용한다.
    - 📌 def has_permission
        - class IsAdminOrIsAuthenticatedReadOnly에서의 has_permission 함수는 로그인하지 않은 사용자(!)와 함께 로그인 사용자가 GET요청을 할 때, admin 사용자거나 가입일이 7일 이상인 사용자가 요청할 경우 등으로 여러 조건에서 권한 처리를 할 것에 대한 내용이 들어 있다.
    - 📌 GenericAPIException
        - 이 클래스는 관리자 계정 및 로그인한 계정에 대한 설정이 주를 이루고 있는 퍼미션이지만, 로그인하지 않은 사용자에게도 처리가 필요한 경우를 상정해 GenericAPIException 클래스를 사용하여 처리해준다.

##### 👨‍💻 관리자/로그인 사용자 권한설정에서의 def has_permission
함수 has_permission에서의 로직은 다음과 같다.
    1. request.user를 변수 user에 초기화한다.
    2. request.user의 메서드 is_authenticated를 사용하여 사용자가 로그인 되어 있는지 확인한다.
        - if 사용자가 로그인 되어있지 않다면:
        - detail = '서비스를 이용하기 위해 로그인 해주세요' 메시지를 response 변수에 dict로 담아 초기화 한다
        - GenericAPIException을 호출하여 401코드와 detail을 담아 raise한다.
    2. 로그인 된 사용자가 GET을 요청한다면 True를 반환한다.
        - if 사용자로그인 이면서 요청한 HTTP METHOD가 SAFE_METHOD라면 True 반환
    3. admin 사용자거나 가입일이 7일 이상 된 사용자가 요청한다면 True를 반환한다.
        - if 사용자로그인 이면서 관리자계정 이거나 가입일 7일이 넘은 계정이라면:
            - user의 UserModel 중 join_date 가
            - datetime 라이브러리의 datetime.now().date 현재 시간대의 날짜값에 timedelta(days=7) 7일의 시각을 뺀 값 보다 작다면:
        - True 반환
    4. 세가지의 분기를 모두 통과한다면(어디에도 해당되지 않음) False 반환

#### 👨‍💻 **class GenericAPIException**
class IsAdminOrIsAuthenticatedReadOnly에서 사용된 GenericAPIException을 호출하기 위해서는 해당 클래스가 있어야겠죠?

    1. GenericAPIException의 클래스는 APIException을 가져와 상속받는다.
    2. 내부 함수는 ```__init__```을 사용한다.
        - 함수의 인자로는 self, status_code, detail=None, code=None을 받는다.
        - class IsAdminOrIsAuthenticatedReadOnly의 has_permission 함수에서 GenericAPIException 클래스를 호출하고, status_code와 detail을 인자로 담아 보낸다.
    3. ```__init__```에서 status_code를 인자로 받아 self.status_code에 초기화한다.
    4. APIException의 super()함수로 ```__init__```에 detail과 code를 넣는다.

작성된 GenericAPIException은 호출되고, 다시 has_permission의 분기를 거쳐 False를 반환하게 된다.


## 🎯 user APP

## 🎯 blog APP

## 🎯 product APP