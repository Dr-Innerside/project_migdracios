# 뇌피셜 코드리뷰

## 🎯 user APP
### 💾 serializers.py
#### 👨‍💻 **class HobbySerializer**
HobbySerializer는 user.models의 Hobby를 참조하여 view에서 호출했을 때 반환할 데이터를 정제한다.

- 💡 class Meta
    - 참조할 모델은 HobbyModel(from .models import Hobby as HobbyModel)
    - 반환할 필드는 취미이름(name)과 취미를 선택한 사용자들(same_hobby_users)이다.
- 💡 same_hobby_users
    - HobbyModel에는 취미이름이라는 필드만 존재한다.
    - HobbyModel은 UserProfileModel에서 ManyToMany관계 필드로 참조한다.
    - 한 명의 유저는 한개 혹은 복수의 취미를 가지고 있을 수 있다.
    - same_hobby_users는 특정 취미 하나를 선택한 유저들을 보여줄 수 있게 하기 위해 사용한다.
    - 라이브러리 rest_framework의 serializers 메서드 중 SerializerMethodField로 Hobby 모델에 존재하지 않는 필드를 추가한다.
    - 현재는 사용할 수 있는 상태가 아님
- 💡 get_same_hobby_users
    - serializers.SerializerMethodField로 선언한 변수 same_hobby_users를 함수 get_선언한 변수 이름(self, obj)로 선언하여 리턴 값을 넣어주어야만 필드에서 사용할 수 있다.
    
##### 👨‍💻 get_same_hobby_users
get_same_hobby_users 함수는 SerializerMethodField로 선언한 변수 same_hobby_users를 받아 특정 취미를 선택한 사용자를 필드로 보내기 위해 작성되었다.

- 함수는 get_ SerializerMethodField로 선언한 변수 이름 이라는 규칙이 존재한다.
- 함수는 self, obj를 인자로 받는다.
    - obj는 view에서 시리얼라이저로 요청할 때 들어오는 값이 된다.
- context["request"].user 로 사용자를 받는다.
    - 역참조 결과값에서 사용자 데이터를 배제하기 위해 선언
- UserModel로 생성된 userprofile_set 메서드를 활용하여 OneToOne 관계에 있는 사용자 상세정보 모델을 역참조 한 데이터에서 사용자 값을 뺀 것을 반복문으로 슬라이싱하여 사용자의 실명만을 리스트에 담아 반환한다.
    - obj.userprofile_set이 UserProfile 모델에 존재하는 취미 필드를 중심으로 역참조한 데이터를 의미한다.
    - exclude(user=user)가 사용자 데이터를 배제하겠다는 메서드임을 의미한다.
    - for up in obj~ 가 반복문으로 나온 사용자 이름을 슬라이싱 함을 의미한다.
    - [up.user.fullname for up in obj~] 는 List Comprehension으로 반복문으로 나온 사용자 데이터 하나하나를 UserModel의 실명으로 받아 리스트로 저장한다는 것을 의미한다.
- 메타 클래스에서 반환할 필드에 same_hobby_users를 담아, 함수가 실행되어 역참조된 데이터를 반환한다.

#### 👨‍💻 **class UserProfileSerializer**
UserProfileSerializer는 user.models.py의 UserProfile 모델을 참조하여 반환할 데이터를 지정한 시리얼라이저다.

- 💡 class Meta
    - 유저프로필 시리얼라이저의 메타 클래스는 UserProfile 모델 중, 소개/생일/나이/취미/취미리스트 등을 반환한다.
- 💡 hobby
    - UserProfile에서 ManyToMany관계에 해당하는 취미 필드를 가져오기 위해서 HobbySerializer를 가져와 many=True로 참조한다.
        - read_only=True 옵션을 넣어 수정할 수 없도록 한다.
- 💡 get_hobbys
    - get_hobbys는 rest_framework 라이브러리의 serializers 중 ListField를 가져온 것이다.
    - ListField는 취미 리스트를 가져온다.
    - ❓ HobbySerializer 로 선언한 변수 hobby를 get_으로 가져와 리스트로 보여준다.

#### 👨‍💻 **class UserSerializer**
UserSerializer는 user.models의 User 모델을 참조하여 반환할 데이터를 지정한 시리얼라이저다.

- 💡 userprofile
    - 변수 userprofile은 UserProfileSerializer 클래스를 의미한다.
        - 반환할 필드에 이름 userprofile을 지정해주어 UserProfileSerializer에서 반환하는 모든 필드를 추가로 붙인다.
- 💡 articles
    - 변수 aricles는 ArticleSerializer 클래스를 가져왔다.
        - blog.models의 Article 모델 중 author 필드는 User 모델을 OneToMany로 참조한다.
        - many=True 를 작성해주어 한 명의 유저가 작성한 여러 개의 아티클을 조회할 수 있다.
        - ❓ source=article_set 를 작성해서 역참조를 사용해 아티클을 작성한 사용자를 조회한다.

- 💡 def validate
    - ❓ 함수 validate는 
- 💡 def create
- 💡 def update
- 💡 class Meta
- 💡 extra_kwargs