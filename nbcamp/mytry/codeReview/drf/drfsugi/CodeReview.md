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
product APP에서는 쇼핑몰에 사용되는 상품과 관련된 기능이 작성되어 있다.
- 📌 admin.py
    - product 모델을 어드민페이지에서 조회할 수 있도록 등록되어 있다.
- 📌 models.py
    - 상품 모델인 class Product가 작성되어 있다.
- 📌 urls.py
    - product/로 시작하는 url이 작성되어 있다.
        - ProductView라는 view를 product/에서 조회한다.
        - 오브젝트 id를 참조하는 ProductView를 product/<obj_id>/에서 조회한다.
- 📌 views.py
    - 상품 조회/등록/수정/삭제와 관련한 API가 작성되어 있다.
    - ProductView라는 클래스에서 HTTP METHOD get/post/put/delete로 구분되어 각 기능이 메서드에 맞게 작성되어 있다.
- 📌 serializers.py
    - 상품 모델 Product 에서 보내줄 데이터를 정제한다.
    - class ProductSerializer에 작성되어 있다.
        - 모델 내부의 모든 필드를 참조한다.

## 🎯 blog APP

## 🎯 product APP