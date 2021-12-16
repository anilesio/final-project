from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    url(r'^$',index, name="index" ),
    url(r'^categorias$',categorias, name="categorias" ),
    url(r'^cursos$',cursos, name="cursos" ),
    url(r'^cursosFaculdade$',cursosFaculdade, name="cursosFaculdade" ),
    url(r'^sejaProfessor$',sejaProfessor, name="sejaProfessor" ),
    url(r'^estatisticas$',estatisticas, name="estatisticas" ),
    url(r'^politica-uso$',politicaUso, name="politica-uso" ),
    url(r'^detalhesCurso/(?P<pk>\w+)/$', detalhesCurso, name='detalhesCurso'),
    url(r'^perfil-professor/(?P<pk>\w+)/$', perfilProfessor, name='perfil-professor'),

    url(r'^ajuda$', ajuda, name="ajuda"),
    url(r'^faqs$', faqs, name="faqs"),
    url(r'^magazine$', magazine, name="magazine"),
    url(r'^artigos/(?P<pk>\w+)/$', artigos, name='artigos'),
    url(r'^ver_artigo/(?P<pk>\w+)/$', ver_artigo, name='ver_artigo'),
    url(r'^ver_magazine/(?P<pk>\w+)/$', ver_magazine, name='ver_magazine'),
    url(r'^magazine_categorias/(?P<pk>\w+)/$', magazine_categorias, name='magazine_categorias'),
]
