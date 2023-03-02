# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser

# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'Country', 'City')

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )