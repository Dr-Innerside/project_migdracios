# Django Rest Framework day4

## 📌 4일차 강의 목표
- 외래 키에 대한 이해
- 역참조에 대한 이해
- drf Serializer에 대한 이해

### 🚩 외래키에 대한 이해
외래 키의 종류
#### 1. ForeignKey
- one-to-many 형태로 특정 테이블에서 다른 테이블을 참조할 수 있다.
- 예시로 영화관과 시청자의 관계를 나타낼 때, 시청자 테이블에서 영화관 테이블을 FK로 참조할 수 있다.

#### 2. OneToOneField
- one-to-one 형태로 FK와 동일하지만, 일대일 관계만 가능하다.
- 사용자 계정 테이블과 사용자 프로필 테이블이 별도로 존재할 때, 계정 테이블을 프로필에서 일대일로 관계를 맺을 수 있다.

##### 🕵️‍♀️ 사용자 프로필 모델 생성하기(O:O)
- 유저의 상세정보를 담고 있는 UserProfile이라는 테이블을 작성한다.
- User 테이블에서는 이름, 이메일, 비밀번호 이외의 자기소개, 생일 등의 정보를 저장한다.
- User 테이블에서 위의 내용을 저장하지 않는 것은 User에서는 보안 상 민감한 정보만을 담고 이외의 프로필 상세 내용을 UserProfile에서 다루는 측면이 있음
- 원하는 필드를 생성하고 난 뒤, 사용자-사용자프로필 관계를 참조하여 User를 참조하는 OneToOneField를 생성한다.
- FK에 unique=True 어트리뷰트를 추가한 것과 유사하지만 일반적으로 OneToOneField로 사용한다.

```python
# user detail info table
class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="유저", on_delete=models.CASCADE)
    introduction = models.TextField("자기소개")
    birthday = models.DateField("생일")
    age = models.IntegerField("나이")
    hobby = models.CharField("취미", max_length=50)

    def __str__(self):
    return f"{self.user.username} 님의 프로필입니다"

# user - user detail : 1:1
# 한 유저가 두 프로필을 가질 수는 없음
```


#### 3. ManyToManyField
- many-to-many 형태로 한 개의 필드에서 여러 개의 테이블을 참조할 수 있다.
- 영화라는 테이블에서 카테고리 테이블의 오브젝트를 참조하고 싶을 때, many-to-many 관계를 사용해 두 개 이상의 오브젝트를 참조할 수 있다.
- O:O, O:M 형태는 하나의 대상 만을 바라보고 있지만, M:M은 여러 개의 대상을 바라보고 있을 수 있다!

#### Hobby <-> UserProfile(M:M)
1. 취미 이름이 담긴 Hobby Model 생성
2. UserProfile Model에서 Hobby를 ManyToMany로 참조
3. Hobby의 on_delete 옵션은 SET_NULL
4. FK 옵션에 Null 허용

```python
# hobby table
class Hobby(models.Model):
    name = models.CharField("취미 이름", max_length=20)
        
# user detail info table
class UserProfile(models.Model):
    user = models.OneToOneField(to=User, verbose_name="유저", on_delete=models.CASCADE, primary_key=True)
    ...
    hobby = models.ManyToManyField(Hobby, verbose_name="취미", null=True)
    ...
```

⚠ 왜 CASCADE가 아닐까?
- User <-> UserProfile 의 경우, 참조 중인 User 오브젝트가 삭제되면 UserProfile도 삭제되어야 한다! 그리고 그것을 수행해주는 것이 on_delete=CASCADE
- 그러나 Hobby <-> UserProfile의 경우, 참조 중인 Hobby 오브젝트가 삭제되면 UserProfile도 삭제되어야 하는가? 아니다!
- 따라서 사라진 취미 오브젝트가 사라지면 Null로 비워주는 SET_NULL 옵션을 사용한다!

### 🔥 역참조에 대한 이해
#### 🤔 역참조가 뭔데?
- 취미<->사용자프로필의 관계에서 특정 사용자가 선택한 취미를 가져온다면 그것은 정참조라고 한다.
- 따라서 정참조를 사용해서 사용자의 취미 오브젝트를 가져올 수 있다.
- 반대로 사용자프로필에서 취미를 하나 특정해 이를 선택한 유저 목록을 가져오는 것은 반대로 역참조라고 한다.
- 따라서 역참조를 사용해서 취미를 고른 사용자 오브젝트를 가져올 수 있다.

#### 🤔 역참조를 왜 써야하는데?
- 만약 특정 취미를 선택한 사용자 오브젝트 리스트를 가져오고 싶다면? 정참조로는 가져올 수가 없다..!
- 따라서 역참조를 사용해야 하는 경우가 존재하며, 개념에 대한 이해가 필요하다! 

#### 📜 역참조에 대한 이해
- 외래키를 사용해 참조하는 object를 역으로 찾을 수 있다.
- 외래 키 지정 시 related_name 옵션을 사용해 역참조시 사용될 이름을 지정할 수 있다.
    - models.py에서 related_name을 user_hobby로 지정했다면 hobby.user_hobby와 같이 사용한다.
- 역참조 시 "relate_name"_set 을 사용하여 역참조를 지정해 준다.
    - OneToOneField의 경우에는 예외적으로 _set을 붙이지 않는다!

```python
user_profile.hobby # 정참조
hobby.userprofile_set 
# hobby를 참조하고 있는 UserProfile 테이블의 object를 가져옴
```

```python
# 사용자 정보 조회
    def get(self, request):
        user = request.user

        # 정참조
        # user_profile = UserProfile.objects.get(user=user)
        # hobbys = user_profile.hobby.all()

        # 역참조
        # User모델에는 없는 userprofile을 사용해서 가져옴
        hobbys = user.userprofile.hobby.all()   # OneToOneField는 예외로 _set을 붙이지 않음
        hobbys = str(hobbys)
        
        return Response({"message": f"get method! && hobbys->{hobbys}"})
```

#### ✍ 역참조를 활용해 나와 같은 취미를 가진 사람을 찾는 코드
```python
from django.db.models import F

def get(self, request):
    user = request.user
    hobbys = user.userprofile.hobby.all()
    for hobby in hobbys:
        # exclude : 매칭 된 쿼리만 제외, filter와 반대
        # annotate : 필드 이름을 변경해주기 위해 사용, 이외에도 원하는 필드를 추가하는 등 다양하게 활용 가능
        # values / values_list : 지정한 필드만 리턴할 수 있음. values는 dict로 return, values_list는 tuple로 return
        # F() : 객체에 해당되는 쿼리를 생성함
        hobby_members = hobby.userprofile_set.exclude(user=user).annotate(username=F('user__username')).value_list('username', flat=True)
        hobby_members = list(hobby_members)
        print(f"hobby : {hobby.name} / hobby members : {hobby_members}")

# result print
"""
hobby : 산책 / hobby members : ['user1']
hobby :  음악감상 / hobby memebers : ['user1', 'user2']
hobby : 스쿠버다이빙 / hobby memebers : ['user2']
hobby : 여행 / hobby memebers : ['user2']
"""
```

역참조를 활용하여 특정 취미를 선택한 사용자를 불러오는 기능이 구현되어 있다.

**🕵️‍♀️ 로직 작성 순서는 다음과 같다.**
1. user.userprofile.hobby.all()
- OneToOne으로 참조하는 UserProfile 테이블이 userprofile로 바뀌어 request.user의 메서드로 바로 바로 역참조가 가능하다
- _set을 쓰지 않고 user.userprofile에 저장된 내용 중 hobby의 모든 오브젝트들을 가져오는 구문
2. for hobby in hobbys:
- 모든 취미 오브젝트들을 반복문으로 슬라이싱한다.
3. 특정 취미의 데이터를 역참조하는 사용자 with exclude, annotate
- hobby의 userprofile_set이라고 작성하여 역참조 및 UserProfile object로 return
- exclude(user=user)라고 작성하여 그 중 입력받은 사용자는 제외
- annotate(username=F('user__username'))이라고 작성하여 쿼리셋 안의 오브젝트를 이름을 변경하여 쿼리로 저장
    - annotate(이름을 바꿀 내용)
    - username(username이라는 메서드로 생성)=F(UserProfile 안의 user 항목-->은 User모델의 username)
    - 쿼리셋 오브젝트가 아닌 username=user1 의 쿼리, 튜플 형태로 저장
4. .values_list를 작성하여 username이라고 저장된 데이터를 모두 모아 리스트로 저장
5. flat=True를 작성하여 튜플을 해제한 쿼리셋 형식으로 저장됨
6. list(hobby_members)를 작성하여 쿼리셋을 사용할 수 있게 리스트로 변환

⚠ 위의 구문은 숙지하고 있어야 하지만, Serializer로 대체되는 경우가 많다.

## 💡 dir 메서드와 디버깅
- dir 메서드는 인자에서 사용할 수 있는 클래스 및 함수를 모두 출력한다.
- 역참조 예시를 들어 선언해주지 않은 userprofile은 어디서 나왔는가? 하고 찾아보기위해 dir을 출력해본다
```python
user = request.user # 입력받은 유저
print(dir(user))    # 유저에서 사용할 수 있는 메서드 보기
```
- dir이 디버깅에 유리한 점은 당장 사용할 수 있는 메서드 중 명확하게 보이는 것을 
- 문서를 참조하여 작성하는 것보다 빠르게 적용할 수 있다는 점에 있다.

## 💡 eval 메서드
- eval 메서드 내부의 인자를 문자열로 작성하여 메서드를 적용할 수 있다.
- dir 메서드와 병용하여 디버깅을 수월하게 시도할 수 있다.
- ❌ 그러나 delete와 같은 메서드가 포함 될 수 있어 주의해야 하며, 또한 디버깅 이외의 실제 프로젝트 내부에서는 사용해서는 안된다!!
    - 악의적 사용자(해커)가 임의로 eval 메서드의 가능성을 감안하여 수 많은 메서드를 입력 값에 시도하게 된다면,
    - 개발자의 의도 이외의 부정적 방향으로 프로젝트가 수정될 가능성이 있기 때문이다!

```python
print(eval("1+1")) # 와 같은 모습으로 식 계산도 가능하다.
```
```python
# dir, eval 메서드를 사용해 작동하는 메서드 확인하기

hobbys = user.userprofile.hobby
for command im dir(hobbys):
    try:
        print(f"command: {command} / ", eval(f"hobbys.{command}()"))
        print(f"command: {command} / ", eval(f"hobbys.{command}"))
    except:
        pass
```

## ⭐ DRF Serializer
Serializer, 직렬화란?
- django의 object, queryset 인스턴스 등 복잡한 데이터들을 JSON같은 다른 컨텐츠 유형으로 쉽게 변환할 수 있음

### 🤔 Serializer를 사용했을 때의 장점은 도대체 무엇인가?
- 데이터를 가져오고 리턴해주는 것이라는 측면을 볼 때는 '굳이 써야하나?' 라는 생각이 든다.
- 그러나 가져올 데이터가 둘 이상의 테이블부터 세세하게 데이터를 추려내 하나로 묶어 보여주고 싶다면?
- 이런 데이터 정제를 view에서 사용하면 가독성도 별로 좋지 않을 것이며, 더욱 복잡해 질 것이다!
- Serializer를 사용하는 것으로 복잡한 데이터를 정제하는데 최적화 되어 있으며, 사용성, 가독성 또한 뛰어나다!
- OPEN API인 미세먼지 데이터 등과 유사한 JSON 형식의 데이터를 출력할 수 있다!

### 📜 Serializer 사용법
🕵️‍♀️ 사용예시

```python
# serializers.py
from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
```
```python
# views.py
from .serializers imoprt UserSerializer

def get(self, request):
    return Response(UserSerializer(request.user).data)
```
1. serializers.py 파일 생성
2. serializer 클래스 생성
- 명칭은 크게 중요하지 않으나,
- 사용자 직렬 클래스라면 User + Serializer 등의 컨벤션을 지키면 가독성이 좋다

3. meta 클래스 생성
4. model 어트리뷰트 생성
- 적용할 모델을 선택한다. import로 모델을 미리 가져와줘야 사용할 수 있다.

5. fields 어트리뷰트 생성
- 적용할 필드를 선택한다. 모든 것을 가져오고 싶을때는 ```"__all__"```을 사용한다.
- 가져오고 싶은 필드가 있다면 ```["field1", "field2"]``` 와 같이 작성한다
- 필드는 만들고 싶은 대로 만드는 것이 아니다! 작성되어 있는 필드를 오타 없이 가져와야 한다.

6. view에서 import serializer 
- 실제 view에서 API를 작성하기 위해서 Serializer를 사용하는 것이므로 임포팅!

7. return Response에 serializer 적용하기
- 작성한 Serializer를 Response에 적용할 데이터를 인자로 담는다.
- ``` return Response(UserSerializer(user).data) ``` 과 같이 사용하며, request.user였던 변수 user를 인자로 가져간 것.
- 📌 보내고 받는 데이터 방식은 JSON 이기 때문에 serializer().data 형식으로 항상 작성하게 된다!

### 🔥 OneToOneField 데이터를 Serializer 추가
입력받은 사용자의 정보(아이디,비밀번호,이메일,풀네임 등)에 사용자 프로필정보(생일, 소개, 나이 등)를 추가로 가져올 것이다.

```python
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age"]

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer() # object

    class Meta:
        model = UserModel
        fields = ["username", "email", "fullname", "join_date", "userprofile"]
```

⚠ OneToOneField의 경우에는 Serializer로 가져온 값이 object이다!
- OneToOne 관계로 가져온 경우에는 _set을 추가하지 않고도 바로 참조가 가능하기 때문에
- UserSerializer 클래스 Meta fields에 userprofile 이름으로 그대로 가져온다!
- 이렇게 바로 사용할 수가 있다!

### 🔥 ManyToManyField 데이터를 Serializer로 추가
사용자 프로필 중에서 ManyToMany 관계를 갖는 필드 취미를 HobbyModel에서 추가로 가져오고 싶다!

```python
class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = HobbyModel
        fields = ["name"]

class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True) # input data가 queryset일 경우 many=True 옵션 필요

    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age", "hobby"]
```

⚠ ManyToManyField의 경우에는 Serializer로 가져온 값이 queryset이다!
- ManyToMany 관계로 가져온 경우, 시리얼라이저의 데이터 형식은 queryset이기 때문에 바로 가져다 쓸 수 없다.
- 마찬가지로 프로필의 메타 필드에 취미 필드를 추가해준 뒤, 취미 필드를 시리얼라이저로 바꿔주면서 many=True 를 추가로 작성해 주어야 한다.
- 이런 취미 필드를 유저 시리얼라이저에서도 사용할 수 있지만, 추가적인 작업이 필요하다!

### 🔥 Serializer를 사용하여 같은 취미를 가지고 있는 유저를 역참조로 가져오기
- 원래는 시리얼라이저 메타의 필드는 없는 이름은 작성할 수 없지만, SerializerMethodField()를 사용하여 추가해줄 수도 있다!

```python
class HobbySerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()
    def get_same_hobby_users(self, obj):
        # return "TEST" # 하드 코딩
        user_list=[]
        # print(f'obj->{obj}, type(obj)->{type(obj)}') # hobby model의 object
        # print(dir(obj)) # userprofile_set 이 있다?!
        # print(obj.userprofile_set.all())
        '''
        방법 1. 반복문
        for user_profile in obj.userprofile_set.all():
            user_list.append(user_profile.user.username)
        return user_list
        '''
        # 방법 2. List Comprehension
        return [up.user.username for up in obj.userprofile_set.all()]

        class Meta:
        model = HobbyModel
        fields = ["name", "same_hobby_users"]
```

1. SerializerMethodField 변수 same_hobby_users 추가하기
2. def get_변수 함수 추가하기
- 반드시 변수 이름 앞에 ```get_```가 들어 있어야 한다!!
- 함수는 self, obj를 인자로 받는다
- 리턴 값에 무엇을 넣느냐에 따라 유동적인 값을 넣을 수 있는 필드를 만들 수 있다.
3. 함수 get_same_hobby_users 역참조 데이터 데이터 정제, 리턴
- obj로 받아온 값은 등산, 운동 등등의 취미 이름들이다.
- dir(obj)로 사용할 수 있는 메서드를 찾는다. M:M으로 참조 중인 UserProfile을 역참조 할 수 있는 userprofile_set이 존재한다!
- 각 취미를 가지고 있는 유저를 역참조로 가져오도록 obj.userprofile_set.all() 메서드를 각각 취미마다 볼 수 있게 반복문을 사용한다.
- 빈 리스트에 슬라이싱 된 쿼리셋을 어펜딩한다.
- 취미마다 선택한 유저들의 데이터가 담긴 리스트를 리턴한다.
4. 메타 필드에 same_hobby_users 추가하기
5. view에서 UserSerializer(user) 로 Response를 return 한다.
- UserSerializer->UserProfileSerializer->HobbySerializer 를 모두 타고 가면서 정제된 하나의 JSON 데이터를 받아 볼 수 있다.

### 🔥 request.user가 아닌 회원가입한 전체 유저를 대상으로 데이터 가져오기
```python
# views.py

def get(self, request):
    all_users = UserModel.objects.all()
    return Response(UserSerializer(all_users, many=True).data)

```
1. 전체 유저를 쿼리셋으로 받아오기
2. 전체 유저 데이터가 한 개가 아니므로 return Response에 many=True 작성

### 💡 Serializer source를 사용해 JSON 데이터 필드 이름 변경하기
```python
class UserSerializer(serializers.ModelSerializer):
    user_detail = UserProfileSerializer(source="userprofile") # object

    class Meta:
        model = UserModel
        fields = ["username", "email", "fullname", "join_date", "user_detail"]
```

- Serializer source 속성으로 원래 필드를 지정하고, 변수 이름은 원하는 이름으로 변경한다.
- 메타 필드에 변수를 넣어준다.

## 🚩 permission_classes를 활용한 접근 권한 설정
### 📜 permission 라이브러리 클래스 확인하기
라이브러리를 타고 들어가기
- OperationHolderMixin
- SingleOperandHolder
- BasePermissionMetaclass
- AllowAny
- IsAuthenticated
- IsAdminUser
- IsAuthenticatedOrReadOnly
- DjangoModelPermissions
- DjangoModelPermissionsOrAnonReadOnly 
...

### 🕵️‍♀️ AllowAny
- 무조건 True 반환

### 🕵️‍♀️ IsAuthenticated
- is_authenticated 메서드 확인 후 Bool 반환

### 🕵️‍♀️ IsAdminUser
- is_staff 메서드 확인 후 Bool 반환

### 🕵️‍♀️ IsAuthenticatedOrReadOnly
- request.method in SAFE_METHOD 즉, http method 가 get이거나
- 인증된 사용자라면 True 반환

### ✍ 퍼미션의 이해
- 퍼미션 라이브러리를 타고 들어가서 다양한 permission 조건들이 존재 한다는 것을 알 수 있다.
- 클래스를 확인해서 커스텀 퍼미션을 생성할 수도 있다.
    - 예시로, 가입 7일 이상인 사용자만 True를 반환하는 퍼미션
- 퍼미션은 하나 뿐만이 아닌 둘 이상, 혹은 전체 프로젝트에서 모두 사용하는 범용성이 있으므로, 하나의 앱 안이 아닌 프로젝트에서 작성한다!

### 🚩 커스텀 퍼미션 작성하기!
1. 프로젝트에 permissions.py 파일을 생성한다.
2. 라이브러리의 아무 퍼미션이나 하나 가져온다!
```python
from rest_framework.permissions import BasePermission

class IsAuthenticated(BasePermision):
    """
    Allow access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
```
3. ⚠ 클래스 이름과 퍼미션에 사용될 로직을 변경한다.
4. views.py에 import 퍼미션
```python
# views.py

from ai.permissions import MyCustomPermission
```
5. 커스텀 퍼미션을 사용할 함수 안에 넣어준다.
```python
def get(self, request):
    permission_classes = [MyCustomPermission]
```

### 🔥 가입일이 7일 이상인 유저에게만 True를 반환하는 커스텀 퍼미션
```python
from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta

class RegistedMoreThanAWeekUser(BasePermission):
    def ha_permission(self, request, view):
        # 사용자 인증 확인
        user = request.user
        if not user or not user.is_authenticated:
            return False
        
        # DateField : 2020-10-01
        # DateTimeField : 2020-10-10 10:22:21

        """
        가입일 : 6/01
        현재 - 7일 : 6/10 - 7 = 6/03
        가입한 날짜로부터 7일 뒤인 6/08일부터 퍼미션은 True가 되므로,
        if 가입일 < 현재 - 7일 : True
        True False 반환하기 때문에 if가 없어도 적용됨!
        """
        print(f"user join date -> {user.join_date}")
        print(f"now date -> {datetime.now().date()}")
        print(f"a week ago -> {datetime.now().date()-timedelta(days=7)}")
        return bool(user.join_date < (datetime.now().date()-timedelta(days=7)))
```