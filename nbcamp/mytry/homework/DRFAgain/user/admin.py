from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import (
    User as UserModel,
    UserProfile as UserProfileModel,
)

class UserProfileInline(admin.StackedInline):
    model = UserProfileModel

class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'fullname', 'email') #디스플레이에 보여질 리스트들
    list_display_links = ('username', ) #디스플레이된 이름의 링크를 어디에 달것인지
    list_filter = ('username','email' ) #필터는 뭐만 보여줄건지
    search_fields = ('username', 'email', ) #말그대로 서치 필드

    fieldsets = (
        ("info", {'fields': ('username', 'password', 'email', 'fullname', 'join_date',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active', )}),)

    filter_horizontal = [] #호리존탈 모엿지

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date', )
        else:
            return ('join_date', )
        
    inlines = (
        UserProfileInline,
    )
    
    # add_fieldsets = (
    # (None, {
    #     'classes':('wide',),
    #     'fields':('email','fullname','password1','password2')}
    #     ),
    # )
# Register your models here.

admin.site.register(UserModel, UserAdmin)
admin.site.register(UserProfileModel)



