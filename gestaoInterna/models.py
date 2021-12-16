from django.db import models
from django.contrib.auth.models import User

# +------------------/ COMUNICAÇÃO /--------------------+

class TipoArtigo(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    data_criacao = models.DateField(auto_now_add=True)
    icone = models.ImageField(default='noticia_default.png', blank=True)
    user = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo

class Artigo(models.Model):
    tipo_artigo = models.ForeignKey(TipoArtigo, on_delete=models.CASCADE, null=False, blank=False)
    titulo = models.CharField(max_length=200, blank=False, null=False)
    descricao = models.TextField()
    estado = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo

class CategoriaMagazine(models.Model):
    titulo = models.CharField(max_length=50, blank=True, null=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    user = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo

class Magazine(models.Model):
    _IMPORTANCIA = (
        ('Destaque', 'Destaque'),
        ('Normal', 'Normal'),
    )
    _ESTADO = (
        ('Activado', 'Activado'),
        ('Desactivado', 'Desactivado'),
    )
    importancia = models.CharField(max_length=30, choices=_IMPORTANCIA, null=True, blank=True, default='Normal')
    estado = models.CharField(max_length=30, choices=_ESTADO, null=True, blank=True, default='Activado')
    titulo_magazine = models.CharField(max_length=100)
    corpo_magazine = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(CategoriaMagazine,on_delete=models.CASCADE,null=False,blank=False)
    foto = models.ImageField(default='noticia_default.png', blank=True)
    user = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo_magazine

class TipoErro(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

class ReportarErro(models.Model):
    _ESTADO = (
        ('Em espera', 'Em espera'),
        ('Visto', 'Visto'),
        ('Resolvido', 'Resolvido'),
        ('Ignorar', 'Ignorar'),
    )
    _TIPO_ERRO = (
        ('Anúncios', 'Anúncios'),
        ('Mensagens', 'Mensagens'),
        ('Upload de fotos', 'Upload de fotos'),
        ('Meu perfil', 'Meu perfil'),
        ('Central de ajuda', 'Central de ajuda'),
    )
    tipo_erro = models.CharField(max_length=40, choices=_TIPO_ERRO, null=False, blank=False,)
    mensagem = models.TextField(null=False, blank=False)
    anexo_foto = models.ImageField(blank=True, null=True)
    estado = models.CharField(max_length=30, choices=_ESTADO, null=True, blank=True, default='Em espera')
    data_criacao = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.mensagem

class Mensagens(models.Model):
    emissor = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)
    receptor = models.CharField(max_length=100, blank=True, null=True)
    mensagem = models.TextField()
    data_registo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensagem