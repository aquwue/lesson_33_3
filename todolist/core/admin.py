from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class PersonAdmin(admin.ModelAdmin):
    list_filter = ('is_staff', 'is_active', 'is_superuser')


admin.site.register(User, UserAdmin)
