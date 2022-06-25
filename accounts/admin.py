
from webbrowser import get
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin 

from .forms import  UserCreationForm, SignUpForm

CustomUser = get_user_model()


class CustomUserAdmin(admin.ModelAdmin):
    add_form = SignUpForm
    model = CustomUser
    list_display = ['email', 'username', 'profile_picture' ]


admin.site.register(CustomUser, CustomUserAdmin)

