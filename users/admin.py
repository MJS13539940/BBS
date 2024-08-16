from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile #models.py 내의 우리가 만든 Profile

# User 모델만 관리자 페이지에 등록하게 되면 프로필 모델은 나타나지 않음
# 프로필 모델을 따로 등록하면 관리자 페이지에서는 볼 수 있지만 유저 테이블과 프로필 테이블이 분리되어 있으므로 불편함
# 아래와 같은 방법으로 두 모델이 같은 모델인 것처럼 함께 볼 수 있음

# Register your models here.

# admin R 과 Profile 을 같은 모델인 것처럼 쓰려고함.
class ProfileInline(admin.StackedInline): #층층이 쌓아서 올릴 수 있는 Inline기능(?)
    model = Profile 
    can_delete = False #User와 1:1로 묶을것이기 때문에 별도의 방법으로 지우지 못하게함.
    verbose_name_plural = 'profile' #모니터링 같은 개념(?): 외부에서 읽을땐 profile로 읽게된다.

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,) #내부에 있을 것
                                #StackedInline을 써서 복수일 수 있기때문에 튜플형태로 저장

admin.site.unregister(User) #기존의 admin페이지의 User를 지운다.
admin.site.register(User, UserAdmin) # User라는 이름으로 대체하는데, 그 내용은 만들어놓은 UserAdmin이다.

#여기까지 하고 나면 admin 페이지에서 User에대한 Profile이 추가됨.