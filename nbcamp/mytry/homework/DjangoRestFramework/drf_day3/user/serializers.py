from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel 


# 사용자 상세정보 시리얼라이저
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = "__all__"


# 사용자 기본정보 시리얼라이저
class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        model = UserModel
        fields = [
            "username", "password", "email", "fullname", "join_date", "userprofile"
        ]