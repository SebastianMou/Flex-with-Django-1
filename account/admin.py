from django.contrib import admin

from .models import UserBase

# Register your models here.
@admin.register(UserBase)
class UserBase(admin.ModelAdmin):
    list_display = ['user_name', 'email', 'is_staff', 'is_active', 'created', 'updated']
    search_fields = ('user_name', 'email', 'is_staff')
    list_filter = ('user_name', 'email', 'is_staff')
