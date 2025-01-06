from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'state', 'is_staff']
    fieldsets = (
        ('Personal info', {'fields': ['username']}),
        ('state', {'fields': ['state']}),
    )


admin.site.register(CustomUser, CustomUserAdmin)