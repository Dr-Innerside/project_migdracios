from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Product as ProductModel
from user.models import User as UserModel

# class AuthorInline(admin.TabularInline):
#     model = UserModel
#     extra: 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'desc') #디스플레이에 보여질 리스트들
    list_display_links = ('title', ) #디스플레이된 이름의 링크를 어디에 달것인지
    list_filter = ('title', ) #필터는 뭐만 보여줄건지
    search_fields = ('title', ) #말그대로 서치 필드

    fieldsets = (
        ("정보", {'fields': ('author', 'title', 'desc', )}),
        ("이미지", {'fields' : ('thumbnail', )}),
        ('게시 기간', {'fields': ('post_date', 'exposure_start_date', 'exposure_end_date', )}),)

    filter_horizontal = [] #호리존탈은 아까 그거야~

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('author', 'post_date', )
        else:
            return ('post_date', )
        
    inlines = [
        # AuthorInline,
    ]

# Register your models here.
admin.site.register(ProductModel, ProductAdmin)
# admin.site.register(ProductAdmin)