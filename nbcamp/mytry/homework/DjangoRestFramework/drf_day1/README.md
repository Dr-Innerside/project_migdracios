# ✍ Django Rest Framework 과제
---
작성일 : 0620, 2022
작성이유 : COPY&PASTE가 아닌, 이해한 것을 바탕으로 직접 작성하기 위해서.

## 🔥 1일차 과제 목록
 1. args, kwargs를 사용하는 예제 코드 짜보기
 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
 3. DB Field에서 사용되는 Key 종류와 특징 서술하기
 4. django에서 queryset과 object는 어떻게 다른지 서술하기

## 1번과제. args, kwargs를 사용하는 예제 코드 짜보기
```python
# 1. args, kwargs를 사용하는 예제 코드 짜보기

list_ = [1,2,3,4,5]
print(f"list_->{list_}")
print(*list_)

def sum_input(*args):
    return sum(args)

sum_result = sum_input(*list_)
print(f"input args and result is ->{sum_result}")

dict_ = {
    "name": "yungsang",
    "age": 29,
    "stuborn": True
}
print(f"dict_->{dict_}")
# print(**dict_)

def who(**kwargs):
    name = kwargs["name"]
    age = kwargs["age"]
    stuborn = kwargs["stuborn"]
    print(f"This is {name}, age is {age}, stuborn is {stuborn}")

who(**dict_)
```
## 2번과제. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
1. mutable
    - 값을 변경할 수 있는 자료형
    - 값을 임의로 변경하더라도 바라보고 있는 주소 값의 위치가 달라지지 않는다.
    - 실제 값이 아닌 주소를 바라보고 있기 때문에, 조회하는 순서가 값이 변경되고 나서라면 다른 값을 출력한다.
    - list, dict 등이 있음
2. immutable
    - 값을 변경할 수 없는 자료형
    - 값을 임의로 변경하면 바라보고 있는 주소에서 할당을 해제하고, 새로운 주소에서 값을 재할당한다.
    - string, tuple 등이 있음

## 3번과제. DB Field에서 사용되는 Key 종류와 특징 서술하기
1. PK(Primal Key)
    - PK는 데이터베이스 테이블에서 반드시 존재해야 하는 키
    - 테이블에 PK가 없거나, 2개 이상 존재할 수 없다.
    - django models.py에서 모델을 만들 때, PK에 대한 작성이 없다면 Auto Increment가 적용된 숫자형 PK가 생성된다.

2. FK(Foreign Key)
    - FK는 현재 테이블에서 다른 테이블의 데이터를 참조하기 위해 존재하는 참조키
    - 모델에서 참조를 원하는 데이터테이블의 PK를 가져와 참조한다.
    - FK는 데이터베이스 관계 중 OneToMany 관계에 해당한다.

3. UK(Unique Key)
    - UK는 데이터 레코드에서 두 개 이상의 값을 허용하지 않는 키
    - 모델 필드에서 unique=True를 작성하였다면, 레코드가 작성될 때 같은 값을 입력했다면 에러가 발생한다.
    - PK는 UK와 같이 테이블 레코드 안에서 같은 두 개의 값을 허용하지 않는다.
    - UK는 주로 사용자 정보 중 아이디, 닉네임 등에 사용된다.

## 4번과제. django에서 queryset과 object는 어떻게 다른지 서술하기
django에서 데이터 테이블에 존재하는 데이터를 ORM을 통해서 추출할 때, 오브젝트와 쿼리셋의 형태의 자료형을 주로 보게 된다.

0. ORM(Object Relational Mapping)
    - ORM은 django와 쿼리형태의 데이터베이스를 연결하여, 데이터베이스 내부의 레코드를 꺼낼 수 있게 하는 django 메서드다.

1. object
    - ORM을 통해서 꺼낸 하나의 모델 레코드를 오브젝트라고 한다.
    - 사용자모델에서 아이디/비밀번호/이름/이메일이 담긴 하나의 오브젝트를 가져올 수 있다.

2. queryset
    - 여러 개의 오브젝트들의 집합을 쿼리셋이라고 한다.
    - 쿼리셋은 하나 혹은 두 개 이상의 오브젝트들로 묶여 있다.
    - "이메일이 gmail.com으로 끝나는 사용자"라는 조건에 부합하는 사용자 데이터를 추출하면 여러 개의 오브젝트들이 추출될 수 있다.
    - 쿼리셋은 리스트로 묶거나, 잘라내서 사용하기도 한다. 
