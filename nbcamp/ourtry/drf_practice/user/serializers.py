from rest_framework import serializers

from .models import User as UserModel


class UserSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__" 
        # 이메일, 실명