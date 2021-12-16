from django.db import models
from django.contrib.auth.models import User
from django.forms.models import BaseInlineFormSet
from professor.models import Curso, Professor
from professor.models import Video
# Create your models here.

TIPO_DOCUMENTO = (
    ('Bilhete de identidade', 'Bilhete de identidade'),
    ('Passaporte', 'Passaporte'),
    ('Carta de condução', 'Carta de condução'),
    ('Atestado de residência', 'Atestado de residência'),
)

GENERO = (
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
    ('Prefiro não informar', 'Prefiro não informar'),
)

class Estudante(models.Model):
    # grupo1
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    nomeCompleto = models.CharField(max_length=300, null=True, blank=True)
    tipoDocumento = models.CharField(max_length=60, null=True, blank=True, choices=TIPO_DOCUMENTO)
    numeroDocumento = models.CharField(max_length=100, null=True, blank=True, unique=True)
    genero = models.CharField(max_length=25, choices=GENERO, null=True, blank=True, default="Masculino")
    # grupo2
    telefone1 = models.CharField(max_length=200, null=True, blank=True, unique=True)
    telefone2 = models.CharField(max_length=200, null=True, blank=True, unique=True)
    emailAlternativo = models.EmailField(max_length=200, null=True, blank=True)
    # grupo4
    morada = models.CharField(max_length=300, null=True, blank=True)
    fotoPerfil = models.ImageField(default="user.png", blank=True, null=True)
    # grupo5
    dataRegisto = models.DateTimeField(auto_now_add = True)
    breveDescricao = models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.user)

class MatriculaCurso(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=True, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    dataRegisto = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.first_name} | {self.curso} | {self.estado}"

class DuvidaAula(models.Model):
    transmissor = models.ForeignKey(User, related_name='transmissor_mensagem', null=True, on_delete=models.CASCADE)
    aula = models.ForeignKey(Video,related_name='aula_mensagem', null=True, on_delete=models.CASCADE)
    mensagem = models.TextField(null=False, blank=False)
    estadoVisto = models.BooleanField(default=False)
    dataEnvio = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ("dataEnvio",)

    def __str__(self):
        return str(self.transmissor.email)

class AvaliarProfessor(models.Model):
    professor = models.ForeignKey(User, related_name='professor_avaliacao', null=True, on_delete=models.CASCADE)
    estudante = models.ForeignKey(User, related_name='estudante_avaliacao', null=True, on_delete=models.CASCADE)
    avaliacao = models.IntegerField()
    dataRegisto = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.estudante} | {self.avaliacao}"
