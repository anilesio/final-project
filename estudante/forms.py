from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User

class EsudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = '__all__'
        labels = {
            'nomeCompleto': ('Nome completo'),
            'numeroDocumento':('Número do documento'),
            'tipoDocumento':('Tipo de documento'),
            'emailAlternativo':('Email alternativo'),
            'breveDescricao':('Descrição'),
            'fotoPerfil':('Foto de perfil'),
            'genero':('Gênero'),
            'telefone1':('Telefone primário'),
            'telefone2':('Telefone secundário'),
        }
        exclude = ['user']
        widgets = {
            'nomeCompleto': forms.TextInput(attrs={'class': 'browser-default estilo-input borda-1', 'placeholder': 'Nome completo'}),
            'tipoDocumento': forms.Select(attrs={'class': 'browser-default estilo-input borda-1'}),
            'numeroDocumento': forms.TextInput(attrs={'class': 'browser-default estilo-input borda-1', 'placeholder': 'Nº do documento'}),
            'genero': forms.Select(attrs={'class': 'browser-default estilo-input borda-1'}),
            'telefone1': forms.TextInput(attrs={'class': 'browser-default estilo-input borda-1', 'placeholder': 'Telefone'}),
            'telefone2': forms.TextInput(attrs={'class': 'browser-default estilo-input borda-1', 'placeholder': 'Telefone alternativo'}),
            'emailAlternativo': forms.TextInput(attrs={'class': 'browser-default estilo-input borda-1', 'placeholder': 'Email'}),
            'fotoPerfil': forms.FileInput(attrs={'class': 'browser-default estilo-input borda-1',}),
            'morada': forms.TextInput(attrs={'class': 'browser-default estilo-input borda-1', 'placeholder': 'Rua, Bairro - Cidade'}),
            'breveDescricao': forms.Textarea(attrs={'class': 'browser-default estilo-input borda-1', 'placeholder': 'Fale um pouco sobre si'}),

        }

class DuvidaAulaForm(forms.ModelForm):
    class Meta:
        model = DuvidaAula
        fields = ['mensagem']
        labels = {
            'mensagem': ('Sua dúvida'),
        }
        widgets = {
            'mensagem': forms.TextInput(attrs={'class': 'browser-default estilo-input'})
        }

class AvaliarProfessorForm(forms.ModelForm):
    class Meta:
        model = AvaliarProfessor
        exclude = ['professor', 'estudante']
        fields = ['professor', 'estudante', 'avaliacao']
