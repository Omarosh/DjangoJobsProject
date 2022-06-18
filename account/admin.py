from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    pass
    model = User
    search_fields = ('email', 'user_type',)
    list_display = ('email', 'user_type', 'gender', 'tags', 'address', 'cv', 'history')
    list_filter = ('email', 'user_name', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('address', 'cv', 'history',)}),
    )
    # formfield_overrides = {
    #     User.history: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    # }
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'user_name', 'password1', 'password2', 'is_active', 'is_staff')}
    #      ),
    # )


# Register your models here.
admin.site.register(User, UserAdmin)
