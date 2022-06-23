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