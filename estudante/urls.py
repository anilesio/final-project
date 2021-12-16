from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    url(r'^$',index, name="index" ),
    url(r'^meu-aprendizado$',meuAprendizado, name="meu-aprendizado" ),
    url(r'^assistir-curso/(?P<pk>\w+)/$', assistirCurso, name='assistir-curso'),
    url(r'^categorias$',categorias, name="categorias" ),
    url(r'^cursos$',cursos, name="cursos" ),
    url(r'^cursosFaculdade$',cursosFaculdade, name="cursosFaculdade" ),
    url(r'^detalhes-curso/(?P<pk>\w+)/$', detalhesCurso, name='detalhes-curso'),
    url(r'^matricula-curso/(?P<pk>\w+)/$', matriculaCurso, name='matricula-curso'),
    url(r'^playlist-curso/(?P<pk>\w+)/$', playlistCurso, name='playlist-curso'),
    url(r'^minha-conta$',minhaConta, name="minha-conta" ),
    # url(r'^enviar-duvida$', enviarDuvida, name="enviar-duvida"),
    url(r'^enviar-duvida/(?P<pk>\w+)/$', enviarDuvida, name='enviar-duvida'),
    url(r'^perfil-professor/(?P<pk>\w+)/$', perfilProfessor, name='perfil-professor'),
    url(r'^eliminar-duvida/(?P<pk>\w+)/$', eliminarDuvida, name='eliminar-duvida'),
    url(r'reportar-erro/$', reportarErro, name='reportar-erro'),
    url(r'sucesso-erro/$', sucessoErro, name='sucesso-erro'),
    url(r'ajuda/$', ajuda, name='ajuda'),
    url(r'ver-artigo/(?P<pk>\w+)/$', verArtigo, name='ver-artigo'),
    url(r'artigos/(?P<pk>\w+)/$', artigos, name='artigos'),

    #avaliar professor



]
