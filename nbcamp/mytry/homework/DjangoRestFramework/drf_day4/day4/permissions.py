from rest_framework.permissions import BasePermission
from datetime import timezone, timedelta

class RegistedMoreThreeDays(BasePermission):
    """
    Allow access only to Registered More than 3days.

    로직
    1. 가입일 파악
    2. 가입일 에서 3일이 지난 시점이 현재 이전인 유저만 True 반환
    """

    def has_permission(self, request, view):
        # 사용자 인증
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return bool(user.join_date>timezone.now()-timedelta(days=3))