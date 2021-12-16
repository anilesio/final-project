from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf.urls.static import static
from .views import *

urlpatterns = [

# ADMIN
    url(r'^$', index, name="index"),
    url(r'^estudantes-gestao$', estudantesGestao, name="estudantes-gestao"),
    url(r'^estudantes-gestao-detalhes/(?P<pk>\w+)/$', estudantesGestaoDetalhes, name='estudantes-gestao-detalhes'),

    url(r'^professores-gestao$', professoresGestao, name="professores-gestao"),
    url(r'^professores-gestao-detalhes/(?P<pk>\w+)/$', professoresGestaoDetalhes, name='professores-gestao-detalhes'),
    url(r'^professores-gestao-cursdo-detalhes/(?P<pk>\w+)/$', professoresGestaoCursoDetalhes, name='professores-gestao-cursdo-detalhes'),
    url(r'^curso-detalhes-gestao/(?P<pk>\w+)/$', detahesCursoGestao, name='curso-detalhes-gestao'),
    url(r'^estado-user/(?P<pk>\w+)/$', estadoUser, name='estado-user'),
    url(r'^cv-professor/(?P<pk>\w+)/$', cvProfessor, name='cv-professor'),
    url(r'^gestao$', gestao, name="gestao"),
    url(r'^magazine-gestao$', magazineGestao, name="magazine-gestao"),
    url(r'^ajuda_admin$', ajudaGestao, name="ajuda_admin"),
    url(r'^ajuda-artigos/(?P<pk>\w+)/$', ajudaArtigos, name='ajuda-artigos'),
    url(r'^eliminar_artigo/(?P<pk>\w+)/$', eliminarArtigo, name='eliminar_artigo'),
    url(r'^magazine-artigos/(?P<pk>\w+)/$', magazineArtigos, name='magazine-artigos'),
    url(r'^eliminar-magazine/(?P<pk>\w+)/$', eliminarMagazine, name='eliminar-magazine'),
    url(r'^ver-artigo-magazine/(?P<pk>\w+)/$', verArtigoMagazine, name='ver-artigo-magazine'),
    url(r'^ver-artigo-ajuda/(?P<pk>\w+)/$', verArtigoAjuda, name='ver-artigo-ajuda'),
    url(r'^editar_ajuda_artigos/(?P<pk>\w+)/$', editar_ajuda_artigos, name='editar_ajuda_artigos'),
    url(r'^editar_magazine_artigos/(?P<pk>\w+)/$', editar_magazine_artigos, name='editar_magazine_artigos'),
    url(r'^editar-categoria-magazine/(?P<pk>\w+)/$', editarCategoriaMagazine, name='editar-categoria-magazine'),
    url(r'^detalhes-erro/(?P<pk>\w+)/$', detalhesErro, name='detalhes-erro'),
    url(r'^erros-reportados$', errosReportados, name="erros-reportados"),
    url(r'^notificacoes/$', notificacoes, name="notificacoes"),
    url(r'^ativar_desativar_conta/(?P<pk>\w+)/$', ativar_desativar_conta, name="ativar_desativar_conta"),
]