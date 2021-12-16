from django.forms import ModelForm
from django import forms
from .models import *


class CursoFrom(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'tituloCurso': forms.TextInput(attrs={'class': 'browser-default estilo-input', 'placeholder': 'Ex.: Curso preparatório de...'}),
            'descricao': forms.Textarea(attrs={'class': 'browser-default estilo-input', 'placeholder': 'O que o seu curso vai abordar?'}),
        }

class VideoFrom(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
        exclude = ['user', 'curso']
        widgets = {
            'video': forms.FileInput(attrs={'class': ''}),
            'descricao': forms.Textarea(attrs={'class': 'browser-default estilo-input borda-1', 'placeholder': 'Descrição'}),
        }

class TurmaFrom(forms.ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'curso': forms.Select(attrs={'class': 'browser-default estilo-input'}),
            'breveDescricao': forms.Textarea(attrs={'class': 'browser-default estilo-input borda-1', 'placeholder': 'Descrição'}),
        }

class CurriculoProfessorForm(forms.ModelForm):
    class Meta:
        model = CurriculoProfessor
        fields = ['tipoCurriculo', 'titulo', 'data_inicio', 'data_fim', 'descricao', 'ficheiro', 'localActuacao']
        exclude = ['user', 'dataRegisto']
        widgets = {
            'descricao': forms.Textarea(attrs={'class': '', 'placeholder': 'Sua mensagem'}),
            'tipoCurriculo': forms.Select(attrs={'class': 'browser-default estilo-input', 'required': 'required'}),
        }