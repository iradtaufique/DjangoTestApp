from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from singupApp.models import Project, Personal, UserAdditionInfo, AdditionInfo


class UserInline(admin.StackedInline):
    model = UserAdditionInfo
    can_delete = False


class NewUser(UserAdmin):
    inlines = [UserInline]


admin.site.unregister(User)
admin.site.register(User, NewUser)
admin.site.register(Personal)
admin.site.register(Project)
admin.site.register(AdditionInfo)
