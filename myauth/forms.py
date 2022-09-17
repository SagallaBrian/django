from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import TextInput, PasswordInput, EmailInput


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']
        widgets = {

            'first_name': TextInput(attrs={
                'class': "form-control forms-fonts",
            }),
            'last_name': TextInput(attrs={
                'class': "form-control forms-fonts",
            }),
            'username': TextInput(attrs={
                'class': "form-control forms-fonts",
            }),
            'email': EmailInput(attrs={
                'class': "form-control forms-fonts",
            }),


        }
