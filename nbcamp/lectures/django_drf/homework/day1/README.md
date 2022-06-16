# Django Rest Framework 과제
---
## 1일차 
---
### args, kwargs를 사용하는 예제 코드 짜보기
```
users = ['황영상', '이민기', '김태인', '김희정']
user_email = {'황영상':'ys20473', '이민기':'psjlmk', '김태인':'kti091', '김희정':'kimheejeong'}
def show_user(*args, **kwargs):
    for user in args:
        print(user, end=' ')
    for email in kwargs.items():
        print(email[1], end=' ')

show_user(*users, **user_email)
```

### mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
mutable 재할당 하지 않아도 같은 메모리 주소 안에서 변경이 가능함. -> list, dict, set, numpy
immutable 재할당 없이 같은 메모리 주소 안에 변경이 불가능하며, 재할당을 하면 새로운 주소를 부여받음. -> tuple, string, int, float, bool

### DB Field에서 사용되는 Key 종류와 특징 서술하기
CharField -> 문자열필드, 문자를 받음(사용자 이름, 닉네임, 설명...)
DatetimeField -> 날짜필드, datetime 값을 받음(작성일자, 업데이트일자...), auto_now_add, auto_now, default 는 한 번에 같이 쓸 수 없다
EmailField -> 이메일필드, 이메일 형식의 값을 받지만 문자열과 동일하다
IntegerField -> 정수필드, 숫자를 받음
PrimaryKey -> PK, 테이블에 반드시 존재해야 함, 중복 값을 허용하지 않음
UniqueKey -> UK, 중복 값을 허용하지 않는 특수한 값(사용자 이름)
ForeignKey -> FK, 다른 테이블에서 사용하기 위해 참조하는 외래키. 게시글 모델에서 사용자 정보 PK를 FK로 참조하기

### django에서 queryset과 object는 어떻게 다른지 서술하기
Object는 앱의 models.py 에 모델에 해당하는 클래스를 하나의 오브젝트 객체라고 함(유저모델, 게시글모델, 좋아요모델...)
Queryset은 위의 오브젝트를 ORM(Object Relational Mapping)을 사용하여 불러낸 데이터의 집합을 의미함