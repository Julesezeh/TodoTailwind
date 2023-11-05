from django.contrib import admin
from .forms import CustomUserChangeForm, CustomUserRegistration
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomAdmin(UserAdmin):
    add_form = CustomUserRegistration
    model = CustomUser
    form = CustomUserChangeForm
    list_display = ["username","email"]


admin.site.register(CustomUser,CustomAdmin)