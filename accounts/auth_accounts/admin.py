from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from .models import MyUser
# Register your models here.
class UserAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "first_name",'last_name','phone', "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ('User_Credentials', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["first_name",'last_name','phone']}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["first_name",'last_name','phone','gender','age','marital_status','children','professional_category','annual_income','annual_net_income_after_any_charges','deposit_amount','country','address','agreement_1','agreement_2', "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email",'id']
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)