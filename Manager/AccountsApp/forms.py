from django.contrib.auth.models import User
from django import forms


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widged = forms.PasswordInput)
    class Meta: #information about the class
        model = Accounts
        fields = ['username', 'password']
