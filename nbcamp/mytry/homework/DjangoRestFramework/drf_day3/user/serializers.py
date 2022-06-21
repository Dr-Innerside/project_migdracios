from multiprocessing import AuthenticationError
from unicodedata import category
from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel 


from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel
from blog.models import Category as CategoryModel


'''
사용자의 정보를 통해 게시글을 가져오려면,
author의 user.username을 참조하는것?

'''

# 카테고리 시리얼라이저
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["category_name"]

# 사용자 댓글 시리얼라이저
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = "__all__"


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
            "username", "password", "email", "fullname", "join_date", 
            "userprofile"
        ]

# 사용자 게시글 시리얼라이저
class ArticleSerializer(serializers.ModelSerializer):
    """
    Article을 받아오면
    카테고리, 작성자를 추가로 시리얼라이저를 받아서
    이름과 카테고리 이름을 보냄
    """

    # print("=====카테고리 시리얼라이저=====")
    
    author = UserSerializer()
    category = CategorySerializer(many=True)
    comment = serializers.SerializerMethodField()
    def get_comment(self, obj):
        # print(f"obj->>{dir(obj)}")
        # print(f"self->{self}")

        # print(obj.comment_set.all())

        comment_list = []
        for target_comment in obj.comment_set.all():
            print(target_comment)
            comment_list.append(
                {
                    "article" : target_comment.article.title,
                    "commenter" : target_comment.commenter.username,
                    "comment_content" : target_comment.comment_content
                }
            )
        print(comment_list)
        return comment_list

        # return [target_comment for target_comment in obj.comment_set.all()]

    class Meta:
        model = ArticleModel
        fields = [
            "author","title","category","content", "comment"
        ]