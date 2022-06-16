# Django Rest Framework 강의 2일차 강의노트

## 가상환경 설정
1. python -m venv venv
- 앞 venv는 가상환경을 사용하겠다는 것, 
- 뒤 venv는 이름이 venv라는 것(관용적으로 venv로 사용)

2. venv/Scripts/activate
- 가상환경을 활성화 해서 안에 pip 라이브러리들을 설치

3. pip freeze > reqirements.txt
- 설치한 pip 목록을 txt파일로 저장
- 매번 라이브러리를 설치하는 것이 아니라 이 파일로 가져와서 바로 설치 할 수 있도록  하는 작업
- 협업에 유용하므로 습관을 들이자

## REST API
프론트엔드에서 백엔드로 보내기 위한 방법
1. GET: 조회
2. POST: 생성
3. PUT: 수정
4. DELETE: 삭제

## FBV, CBV
1. FBV(Function Base View)
- 함수로 view를 생성
- 기존 베이직 강의에서 사용하던 방법

2. CBV(Class Base View)
- 클래스로 view를 생성
- 실무에서 많이 사용
- 클래스 안에 함수를 넣어 하나의 클래스로 get/post/put/delete 를 묶어서 사용할 수 있다
- 이름만 달아주면 자동으로 get/post/put/delete를 알아서 보는건가? -> 그렇다!

## rest_framework.views APIView
- GET/POST/PUT/DELETE의 http method를 타고 들어갈 수 있게 view에서 APIView 클래스를 상속받는다
## rest_framework permissions
- 사용자 별로 접근할 수 있는 권한을 설정해주는 것
- 모두, 로그인된 유저만, 관리자 계정만 등등 규칙이 있음
## rest_framework.response Response
- render, redirect를 대체할 rest 기능
- return Response({}) 로 사용함

## POSTMAN으로 테스트하기
1. 데이터 보내기
- body -> raw -> json 으로 선택
- 파이썬 딕셔너리와 비슷한 json 형식으로 body에 담아서 보냄
- 백엔드에서 **request.data로 받아서 사용 가능