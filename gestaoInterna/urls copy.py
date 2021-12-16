from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf.urls.static import static
from .views import *

urlpatterns = [

# ADMIN
    url(r'^$', index, name="index"),
    url(r'^magazine-gestao$', magazineGestao, name="magazine-gestao"),
    url(r'^ajuda_admin$', ajudaGestao, name="ajuda_admin"),
    url(r'^ajuda_artigos/(?P<pk>\w+)/$', ajudaArtigos, name='ajuda_artigos'),
    url(r'^eliminar_artigo/(?P<pk>\w+)/$', eliminarArtigo, name='eliminar_artigo'),
    url(r'^magazine-artigos/(?P<pk>\w+)/$', magazineArtigos, name='magazine-artigos'),
    url(r'^eliminar_magazine/(?P<pk>\w+)/$', eliminarMagazine, name='eliminar_magazine'),
    url(r'^editar_ajuda_artigos/(?P<pk>\w+)/$', editar_ajuda_artigos, name='editar_ajuda_artigos'),
    url(r'^editar_magazine_artigos/(?P<pk>\w+)/$', editar_magazine_artigos, name='editar_magazine_artigos'),
    # url(r'^add_tipo_artigo$', add_tipo_artigo, name="add_tipo_artigo"),
    url(r'^erros-reportados$', errosReportados, name="erros-reportados"),
    url(r'^notificacoes/$', notificacoes, name="notificacoes"),

    url(r'^ativar_desativar_conta/(?P<pk>\w+)/$', ativar_desativar_conta, name="ativar_desativar_conta"),
]