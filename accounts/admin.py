from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import CustomUser


# @admin.register(CustomUser)
class CustomUserAdmin(DjangoUserAdmin):
    """Define admin model for Custom User model with no email field"""
    create_form = CustomUserCreationForm
    change_form = CustomUserChangeForm
    # Fields to display on the main Admin/Users panel
    list_display = ('email', 'first_name', 'last_name', 'nick')
    search_fields = ('email', 'first_name', 'last_name', 'nick')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'nick')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # Fields to use when adding a new user in Admin panel
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nick', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
