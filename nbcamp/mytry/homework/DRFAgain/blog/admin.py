from django.contrib import admin
from .models import (
    Comment as CommentModel,
    Category as CategoryModel,
    Article as ArticleModel,
)


# Register your models here.
admin.site.register(CommentModel)
admin.site.register(CategoryModel)
admin.site.register(ArticleModel)