from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    url(r'sign_up_anfitriao/$', sign_up_anfitriao, name='sign_up_anfitriao'),
    url(r'cadastrar-estudante/$', cadastrarEstudante, name='cadastrar-estudante'),
    url(r'cadastrar-professor/$', cadastrarProfessor, name='cadastrar-professor'),
    url(r'^cadastrar-curriculo/(?P<pk>\w+)/$', cadastrarCurriculo, name='cadastrar-curriculo'),
    url(r'user-login/$', user_login, name='user-login'),
    url(r'logout-user/$', logout_user, name='logout-user'),
    url(r'sign_tipo_anfitriao/$', sign_tipo_anfitriao, name='sign_tipo_anfitriao'),
    url(r'login-administracao/$', login_administracao, name='login-administracao'),
    url(r'sucesso-cadastro-professor/$', sucessoCadastroProfessor, name='sucesso-cadastro-professor'),
]
