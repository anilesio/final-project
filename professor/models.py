from django.db import models
from django.contrib.auth.models import User
from django.forms.models import BaseInlineFormSet
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

AREA_CIENTIFICA = (
    ('Engenharias', 'Engenharias'),
    ('Ciências Sociais', 'Ciênciais Sociais'),
    ('Ciências Humanas', 'Ciências Humanas'),
    ('Ciências Exactas', 'Ciências Exactas'),
    ('Letras', 'Letras'),
)

TIPO_CURRICULO = (
    ('Curso de especialização', 'Curso de especialização'),
    ('Escolaridade', 'Escolaridade'),
    ('Estágio', 'Estágio'),
    ('Experiência profissional', 'Experiência profissional'),
)

class Professor(models.Model):
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

class Curso(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    tituloCurso = models.CharField(max_length=100)
    descricao = models.TextField()

    ###ESPECIALIDADES###

    #Engenharia
    informatica = models.BooleanField(default = False)
    petroleo = models.BooleanField(default = False)
    geologia = models.BooleanField(default = False)
    geologia_minas = models.BooleanField(default = False)
    construcao_civil = models.BooleanField(default = False)
    agronoma = models.BooleanField(default = False)

    #Ciências da saúde
    medicina_geral = models.BooleanField(default = False)
    medicina_dentaria = models.BooleanField(default = False)
    enfermagem = models.BooleanField(default = False)
    fisioterapia = models.BooleanField(default = False)
    analises_clinicas = models.BooleanField(default = False)
    saude_publica = models.BooleanField(default = False)

    #Letras e Ciências Sociais
    psicologia_forense = models.BooleanField(default = False)
    psicologia_clinica = models.BooleanField(default = False)
    psicologia_trabalho = models.BooleanField(default = False)
    direito = models.BooleanField(default = False)
    ciencias_politicas = models.BooleanField(default = False)
    relacoes_publicas = models.BooleanField(default = False)
    relacoes_internacionais = models.BooleanField(default = False)

    #Gestão
    gestao_empresarial = models.BooleanField(default = False)
    economia = models.BooleanField(default = False)
    gestao_administracao_empresas = models.BooleanField(default = False)

    ###UNIVERSIDADES###
    utanga = models.BooleanField(default = False)
    uan = models.BooleanField(default = False)
    ucan = models.BooleanField(default = False)
    uPiaget = models.BooleanField(default = False)
    uMetodista = models.BooleanField(default = False)
    ista = models.BooleanField(default = False)
    thumb = models.ImageField(blank=True, null=True, upload_to='thumb/')
    videoPreview = models.FileField(blank=True, null=True, upload_to='preview/')
    dataRegisto = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.tituloCurso)

class Video(models.Model):
    curso = models.ForeignKey(Curso, null=True, on_delete=models.CASCADE)
    tituloVideo = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    descricao = models.TextField()
    dataRegisto = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.tituloVideo)

class Turma(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    designacaoTurma = models.CharField(max_length=100, null=False, blank=False)
    breveDescricao = models.TextField(blank=False, null=False)
    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    dataRegisto = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.designacaoTurma)

class CurriculoProfessor(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    tipoCurriculo = models.CharField(max_length=100, blank=False, null=False, choices=TIPO_CURRICULO)
    dataRegisto = models.DateTimeField(auto_now_add = True)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    localActuacao = models.CharField(max_length=100, null=True, blank=True)
    data_inicio = models.DateField(null=False, blank=False)
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    ficheiro = models.FileField(upload_to='ficheiros_cv/', null=True, blank=True)
    def __str__(self):
        return str(self.titulo)