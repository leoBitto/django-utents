from django import forms
from .models import Utent
from django.contrib.auth.forms import UserCreationForm, UsernameField

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Utent
        fields = ("username",)
        field_classes = {'username': UsernameField}