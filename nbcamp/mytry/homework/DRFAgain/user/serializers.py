from rest_framework import serializers

from user.models import (
    User as UserModel,
    UserProfile as UserProfileModel,
)
from blog.models import (
    Article as ArticleModel, 
    Category as CategoryModel, 
    Comment as CommentModel,
)
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = "__all__"

# 3일차 5번과제. 4번의 serializer에 추가로 로그인 한 사용자의 게시글, 댓글을 리턴해주는 기능을 구현해주세요
class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    def get_category(self, obj):
        category_list=[]
        for category in obj.category.all():
            category_list.append(category.name)
        category_list = list(category_list)
        return category_list
    
    class Meta:
        model = ArticleModel
        fields = "__all__"

# 3일차 4번과제. serializer를 활용해 로그인 한 사용자의 기본 정보와 상세 정보를 리턴해 주는 기능을 만들어주세요
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    article = ArticleSerializer(many=True, source="article_set", read_only=True)
    comment = CommentSerializer(many=True, source="comment_set")
    
    class Meta:
        model = UserModel
        fields = ["username", "userprofile", "article", "comment"]


