from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )

from django.views.generic import View
from .forms import UserLoginForm

def register_view(request):
    context = locals()
    template = "home.html"
    return render(request, template, context)


def login_view(request):
    template = "home.html"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    return render(request, template, {"form":form})


def logout_view(request):
    context = locals()
    template = "home.html"
    return render(request, template, context)
