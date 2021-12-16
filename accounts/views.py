from django.shortcuts import render
from django.contrib.auth import (
    authenticate, login, logout, update_session_auth_hash
)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import *
from estudante.models import *
from professor.models import *
from professor.forms import CurriculoProfessorForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib.auth import get_user_model

def sign_up_anfitriao(request):
    return render(request, 'accounts/sign_up_anfitriao.html')

@unautenticate_user
def cadastrarEstudante(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='estudante')
            user.groups.add(group)
            Estudante.objects.create(user=user, nomeCompleto = user.first_name + " " +  user.last_name)
            messages.success(request, 'Conta criada com sucesso' + username)
            return HttpResponseRedirect(reverse('accounts:user-login'))
    context = {'form':form}
    return render(request, 'accounts/cadastrarEstudante.html',context)

@unautenticate_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        usuario = User.objects.filter(username = str(username))
        password = request.POST.get('password')
        if usuario.exists():
            user = authenticate(request, username = username , password = password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login feito')
                messages.info(request, 'Bem-vinda(a)')

                group = user.groups.all()[0].name
                if group == 'estudante':
                    return HttpResponseRedirect(reverse('estudante:index'))
                if group == 'professor':
                    return HttpResponseRedirect(reverse('professor:index'))
                if group == 'admin':
                    return HttpResponseRedirect(reverse('gestao:index_admin'))
            else:
                messages.warning(request, 'Palavra-passe incorreta')
                return render(request, 'accounts/login.html')
        else:
            messages.warning(request, 'Usuário não existe ou campos vazios')
            return render(request, 'accounts/login.html')
    context = {}
    return render(request, 'accounts/login.html',context)


def logout_user(request):
    logout(request)
    messages.info(request, 'Sessão terminada')
    return user_login(request)


def sign_tipo_anfitriao(request):
    return render(request, 'accounts/sign_tipo_anfitriao.html')

@unautenticate_user
def cadastrarProfessor(request):
    form = CreateUserForm(request.POST)
    context = {'form':form}
    if form.is_valid():
        try: 
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            objecto = user
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='professor')
            user.groups.add(group)
            Professor.objects.create(user=user)
            messages.success(request, 'Conta criada com sucesso!')
            messages.success(request, 'Seu username é' + username)
            return HttpResponseRedirect(reverse('accounts:cadastrar-curriculo', kwargs={'pk':int(objecto.id)}))
        except:
            messages.error(request, 'Erro no cadastro')
            return HttpResponseRedirect(reverse('accounts:cadastrar-professor'))

    return render(request, 'accounts/cadastrarProfessor.html',context)

def cadastrarCurriculo(request, pk):
    User = get_user_model()
    objecto = User.objects.get(id = int(pk))

    form = CurriculoProfessorForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        f1 = form.save(commit=False)
        f1.user= objecto
        f1.save()
        messages.success(request, 'Item adicionado')
        return HttpResponseRedirect(reverse('accounts:cadastrar-curriculo', kwargs={'pk':int(objecto.id)}))
    
    context = {
        'objecto':objecto,
        'form':form
        }
    return render(request, 'accounts/cadastrarCurriculoProfessor.html', context)


def login_administracao(request):
    """User sign-in view."""
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Você está logado.")
                    return HttpResponseRedirect(reverse('gestaoInterna:index'))
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Email or password is incorrect."
                )
    args = {
        'form':form
    }
    return render(request, 'accounts/loginAdministracao.html', args)


def sucessoCadastroProfessor(request):
    return render(request, 'accounts/sucesso_cadastro_professor.html',)