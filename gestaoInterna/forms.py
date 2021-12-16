from django import forms

from professor.models import CurriculoProfessor
from .models import *

class TipoArtigoForm(forms.ModelForm):
    class Meta:
        model = TipoArtigo
        fields = ['icone', 'titulo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'browser-default estilo-input', 'placeholder': 'Escreva aqui'}),
        }

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'descricao',]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'browser-default estilo-input', 'placeholder': 'Digite o título'}),
            'descricao': forms.Textarea(attrs={'class': 'browser-default estilo-input', 'placeholder': 'Descrição'}),
        }

class CategoriaMagazineForm(forms.ModelForm):
    class Meta:
        model = CategoriaMagazine
        fields = ['titulo']
        exclude = ['user', 'data_criacao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'browser-default estilo-input', 'placeholder': 'Nova categoria'}),
        }

class MagazieForm(forms.ModelForm):
    class Meta:
        model = Magazine
        exclude = ['user']
        fields = ['titulo_magazine', 'categoria', 'corpo_magazine', 'foto', 'importancia']
        widgets = {
            'titulo_magazine': forms.TextInput(attrs={'class': 'browser-default estilo-input', 'placeholder': 'Título do magazine'}),
            'categoria': forms.Select(attrs={'class': 'browser-default estilo-input',}),
            'importancia': forms.Select(attrs={'class': 'browser-default estilo-input',}),
            'corpo_magazine': forms.Textarea(attrs={'class': 'browser-default estilo-input', 'placeholder': 'Narre aqui'}),
            'foto': forms.FileInput(attrs={'class': 'browser-default estilo-input',}),
        }

class TipoErroForms(forms.ModelForm):
    class Meta:
        model = TipoErro
        fields = ['titulo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'browser-default estilo-input', 'placeholder': 'Informe aqui'}),
        }

class ReportarErroForms(forms.ModelForm):
    class Meta:
        model = ReportarErro
        fields = ['tipo_erro', 'mensagem' ,'anexo_foto']
        widgets = {
            'tipo_erro': forms.Select(attrs={'class': 'estilo-input browser-default', 'placeholder': 'Título do magazine'}),
            'mensagem': forms.Textarea(attrs={'class': 'estilo-input browser-default',}),
            'anexo_foto': forms.FileInput(attrs={'class': 'estilo-input browser-default',}),
        }
    
class MensagensForm(forms.ModelForm):
    class Meta:
        model = Mensagens
        fields = ['mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={'class': '', 'placeholder': 'Sua mensagem'}),
        }