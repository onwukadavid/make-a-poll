from django.contrib import admin
from Accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
# from Accounts.models import Author
from django.contrib.auth import get_user_model

User = get_user_model()
# print(User)

class AuthorAdmin(UserAdmin):

    # model = Author
    # The forms to add and change user instances
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["username", "email", "is_admin", "last_login", "created_at"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["username"]}),
        ("Permissions", {"fields": ["is_active", "is_admin", "is_superuser", "groups", "user_permissions"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email",  "username", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


# Now register the new UserAdmin...
# admin.site.unregister(Group)
admin.site.register(User, AuthorAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.