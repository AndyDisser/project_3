from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUser(UserCreationForm):
    """Extend UserCreatonForm with email address"""
    email = forms.EmailField(required=True, max_length=254)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
