from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class CustomUserRegistration(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("first_name","username","email") 


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username","email","first_name")