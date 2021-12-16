from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sua mensagem'})
        }