from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import get_user_model


class SignupForm(UserCreationForm):
    class Meta:
        # This is the way to access user model generally
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
