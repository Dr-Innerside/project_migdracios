from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta
from rest_framework.exceptions import APIException
from rest_framework import status

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
        
        # DateTimeField와 비교 시
        # (datetime)user.join_date > datetime.now **ERROR**
        # (datetime)user.join_date > timezone.now **ERROR**




class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

class IsAdminOrIsAuthenticatedReadOnly(BasePermission):
    """
    admin 사용자는 모두 가능, 로그인 사용자는 조회만 가능
    """
    SAFE_METHODS = ('GET', )
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response ={
                    "detail": "서비스를 이용하기 위해 로그인 해주세요.",
                }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if user.is_authenticated and user.is_admin:
            return True
            
        if user.is_authenticated and request.method in self.SAFE_METHODS:
            return True
        
        return False