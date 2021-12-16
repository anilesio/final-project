from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'browser-default estilo-input', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'browser-default estilo-input', 'placeholder': 'Primeiro nome'}),
            'last_name': forms.TextInput(attrs={'class': 'browser-default estilo-input', 'placeholder': 'Último nome'}),
            'email': forms.TextInput(attrs={'class': 'browser-default estilo-input', 'type': 'email', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'browser-default estilo-input', 'placeholder': 'Palavra-passe'}),
            'password2': forms.Textarea(attrs={'class': 'browser-default estilo-input', 'placeholder': 'Confirme a sua palavra-passe'}),
        }
