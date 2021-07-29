from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'username', 'created_at', 'cur_task', 'admin', 'is_staff', 'is_active',)
    list_filter = ('email', 'username', 'created_at', 'cur_task', 'admin', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'created_at', 'cur_task')}),
        ('Permissions', {'fields': ('admin', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'username', 'created_at', 'cur_task', 'admin', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username', 'created_at', 'cur_task')
    ordering = ('email', 'username', 'created_at', 'cur_task')

admin.site.register(CustomUser, CustomUserAdmin)