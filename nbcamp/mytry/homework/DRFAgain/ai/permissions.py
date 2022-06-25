from rest_framework.permissions import BasePermission
from rest_framework import status

from django.contrib import auth

from user.models import User as UserModel

from datetime import timedelta
from django.utils import timezone

from rest_framework.exceptions import APIException

class SamIll(BasePermission):
    message = "가입 후 3일 지난 사용자만 사용 가능하다 임마"
    def has_permission(self, request, view):
        '''
        가입일이 3일이 지나면 True
        가입일 +3일이 현재보다 과거 시점이어야함
        가입일 +3일이 현재보다 작음
        '''
        join_date = request.user.join_date
        # register_3day = join_date + timedelta(days=3)

        # 6월 25일 + 3일 timedelta 
        
        return bool(join_date + timedelta(seconds=3) < timezone.now())


# 비로그인 사용자 exception
class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

class IsRegister7DaysOrIsAdmin(BasePermission):
    '''
    4. 기존 article 생성 기능을 유지하되, 
    article은 admin user 혹은 가입 후 7일이 지난 사용자만 
    생성 가능하도록 해주세요
    - 조회는 로그인 한 사용자에 대해서만 가능하도록 설정해주세요
    '''
    
    message = "접근 권한이 없습니다."
    SAFE_METHODS = ('GET',)
    
    def has_permission(self, request, view):
        print("관리자/가입7일유저 퍼미션 너 들어오긴 하니?")
        
        # 비로그인 사용자
        user = request.user
        if not user.is_authenticated:
            response = {
                'detail': '조회를 위해 로그인 해주세용 제발~~'
                }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)
        # 어드민 계정의 경우,
        '''
        로그인 되어있는데, 그게 관리자계정이면? 
        그냥 묻따 True 반환
        '''
        if user.is_authenticated and user.is_admin:
            return True
        print("관리자 분기 통과")
        # 일반 사용자 계정의 경우,
        '''
        1. 세이프 메서드(GET) 만 접근 가능
        2. 가입후 7일이 지난 사용자
        '''
        # 여기는 세이프 메서드랑 상관없는 구간 
        if user.is_authenticated and user.is_admin or \
            user.join_date + timedelta(days=1) < timezone.now():
            print(f"user.join_date-->{user.join_date}")
            return True
        print("가입일 분기 통과")
        
        # 여기서부터 세이프 메서드 봄
        if user.is_authenticated and request.method in self.SAFE_METHODS:
            return True
        
        print("세이프 메서드 분기 통과")
        
        return False