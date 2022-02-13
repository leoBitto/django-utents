from re import template
from django.shortcuts import render, reverse
from django.views import generic
from .forms import CustomUserCreationForm


# Create your views here.
class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("")