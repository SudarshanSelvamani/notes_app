from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy


from .forms import SignUpForm
from notes.models import Notebook


class SignUpView(CreateView):
    template_name = "signup.html"
    success_url = reverse_lazy("login")
    form_class = SignUpForm
