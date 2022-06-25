from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100, label="Last Name")

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email' ,'password1', 'password2']
