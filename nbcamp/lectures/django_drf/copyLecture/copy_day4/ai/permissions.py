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
        
        # DateTimeField와 비교 시
        # (datetime)user.join_date > datetime.now **ERROR**
        # (datetime)user.join_date > timezone.now **ERROR**