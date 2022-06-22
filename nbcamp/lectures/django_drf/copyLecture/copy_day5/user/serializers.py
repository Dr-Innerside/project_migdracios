from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

class HobbySerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()
    def get_same_hobby_users(self, obj):
        # return "TEST" # 하드 코딩
        user_list=[]
        # print(f'obj->{obj}, type(obj)->{type(obj)}') # hobby model의 object
        # print(dir(obj)) # userprofile_set 이 있다?!
        # print(obj.userprofile_set.all())
        '''
        방법 1. 반복문
        for user_profile in obj.userprofile_set.all():
            user_list.append(user_profile.user.username)
        return user_list
        '''
        # 방법 2. List Comprehension
        return [up.user.username for up in obj.userprofile_set.all()]

        
    class Meta:
        model = HobbyModel
        fields = ["name", "same_hobby_users"]

class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True) # input data가 queryset일 경우 many=True 옵션 필요

    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age", "hobby"]

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer() # object

    class Meta:
        model = UserModel
        fields = ["username", "email", "fullname", "join_date", "userprofile"]