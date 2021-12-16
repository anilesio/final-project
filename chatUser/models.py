from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Chat(models.Model):
    transmissor = models.ForeignKey(User, related_name='envia_mensagem', null=True, on_delete=models.CASCADE)
    receptor = models.ForeignKey(User,related_name='recebe_mensagem', null=True, on_delete=models.CASCADE)
    mensagem = models.TextField(null=False, blank=False, default="Sua mensagem")
    estadoVisto = models.BooleanField(default=False)
    dataEnvio = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ("dataEnvio",)

    def __str__(self):
        return str(self.transmissor.email)