from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    url(r'^$',index, name="index" ),
    url(r'^novo-curso$',novoCurso, name="novo-curso" ),
    url(r'^meus-cursos$',meusCursos, name="meus-cursos" ),
    url(r'^detalhes-curso/(?P<pk>\w+)/$', detalhesCurso, name='detalhes-curso'),
    url(r'^detalhes-video/(?P<pk>\w+)/$', detalhesVideo, name='detalhes-video'),
    url(r'^eliminar-video/(?P<pk>\w+)/$', eliminarVideo, name='eliminar-video'),
    url(r'^aviso-curso/(?P<pk>\w+)/$', avisoCurso, name='aviso-curso'),
    url(r'^eliminar-curso/(?P<pk>\w+)/$', eliminarCurso, name='eliminar-curso'),
    url(r'^perfil-estudante$',perfilEstudante, name="perfil-estudante" ),

    url(r'reportar-erro/$', reportarErro, name='reportar-erro'),
    url(r'sucesso-erro/$', sucessoErro, name='sucesso-erro'),
    url(r'ajuda/$', ajuda, name='ajuda'),
    url(r'ver-artigo/(?P<pk>\w+)/$', verArtigo, name='ver-artigo'),
    url(r'artigos/(?P<pk>\w+)/$', artigos, name='artigos'),

    url(r'turmas/$', turmas, name='turmas'),


]
