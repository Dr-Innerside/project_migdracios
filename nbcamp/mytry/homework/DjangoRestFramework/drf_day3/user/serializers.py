from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"