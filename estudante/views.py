from estudante.models import MatriculaCurso
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse
from accounts.decorators import *
from django.contrib import messages
from django.core.paginator import Paginator
from professor.models import Curso, Professor
from .models import Estudante, MatriculaCurso, DuvidaAula, AvaliarProfessor
from .forms import AvaliarProfessorForm, EsudanteForm, DuvidaAulaForm
from professor.models import Video
from django.db.models import Sum
from django.contrib.auth.models import User
from gestaoInterna.models import *
from gestaoInterna.forms import ReportarErroForms

@login_required(login_url='accounts:user-login')
@allowed_users(allowed_roles=['estudante'])
def index(request):
    matriculaCurso = MatriculaCurso.objects.all().filter(user = request.user, estado = True)
    args = {
        'matriculaCurso':matriculaCurso,
        'totMatrivulados':MatriculaCurso.objects.all().filter(user = request.user, estado = True).count()
    }
    return render(request, 'estudante/index.html', args)


@login_required(login_url='accounts:user-login')
@allowed_users(allowed_roles=['estudante'])
def meuAprendizado(request):

    matriculaCurso = MatriculaCurso.objects.all().filter(user = request.user, estado = True)
    args = {
        'matriculaCurso':matriculaCurso
    }
    return render(request, 'estudante/meuAprendizado.html', args)

@login_required(login_url='accounts:user-login')
@allowed_users(allowed_roles=['estudante'])
def assistirCurso(request, pk):
    videosObjecto = Video.objects.get(id = int(pk))
    objecto = Curso.objects.get(id = int(videosObjecto.curso.id))
    videos = Video.objects.all().filter(curso = objecto)

    professor = Professor.objects.filter(user = objecto.user)

    duvidas = DuvidaAula.objects.all().filter(aula = videosObjecto).order_by('-dataEnvio')

    form = DuvidaAulaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            f1 = form.save(commit=False)
            f1.aula = videosObjecto
            f1.transmissor = request.user
            f1.save()
            messages.success(request, "Dúvida enviada")
            return HttpResponseRedirect(reverse('estudante:assistir-curso', kwargs={'pk':int(videosObjecto.id)}))

    args = {
        'objecto':objecto,
        'videos':videos,
        'videosObjecto':videosObjecto,
        'form':form,
        'duvidas':duvidas,
        'professor':professor[0]
    }
    return render(request, 'estudante/assistirCurso.html', args)

def categorias(request):
    return render(request, 'estudante/categorias.html')

def cursos(request):
    professores = Professor.objects.all()
    dados = Curso.objects.all()
    paginacao = Paginator(dados, 10)
    pagina = request.GET.get('pagina')
    cursos = paginacao.get_page(pagina)

    args = {
        'cursos':cursos,
        'dados':dados,
        'professores':professores
    }
    return render(request, 'estudante/cursos.html', args)

def cursosFaculdade(request):
    return render(request, 'estudante/cursosFaculdade.html')

@login_required(login_url='accounts:user-login')
@allowed_users(allowed_roles=['estudante'])
def matriculaCurso(request, pk):
    user = request.user
    curso = Curso.objects.get(id = int(pk))
    video = Video.objects.all().filter(curso = curso)
    try:
        item = video[0]
    except:
        messages.info(request, "Este curso ainda não está completo")
        return HttpResponseRedirect(reverse('estudante:detalhes-curso', kwargs={'pk':int(curso.id)}))

    if MatriculaCurso.objects.all().filter(user = user, curso = curso).exists():
        messages.info(request, "Já está matriculado neste curso")
        return HttpResponseRedirect(reverse('estudante:playlist-curso', kwargs={'pk':int(curso.id)}))
        # return HttpResponseRedirect(reverse('estudante:detalhes-curso', kwargs={'pk':int(curso.id)}))
    else:
        MatriculaCurso.objects.create(user=user, curso=curso)
        messages.success(request, 'Matricula concluída')
    return HttpResponseRedirect(reverse('estudante:playlist-curso', kwargs={'pk':int(curso.id)}))

def detalhesCurso(request, pk):
    objecto = Curso.objects.get(id = int(pk))
    videos = Video.objects.all().filter(curso = objecto)
    totVideos = videos.count()

    professor = Professor.objects.filter(user = objecto.user)

    args = {
        'objecto':objecto,
        'videos':videos,
        'totVideos':totVideos,
        'professor':professor[0]
    }
    return render(request, 'estudante/detalhesCurso.html', args)

def playlistCurso(request, pk):
    objecto = Curso.objects.get(id = int(pk))
    videos = Video.objects.all().filter(curso = objecto)
    totVideos = videos.count()

    args = {
        'objecto':objecto,
        'videos':videos,
        'totVideos':totVideos,
    }
    return render(request, 'estudante/playlistCurso.html', args)

def minhaConta(request):
    user = request.user
    estudante = Estudante.objects.get(user = user)

    form = EsudanteForm(instance=estudante)
    if request.POST:
        form = EsudanteForm(request.POST, request.FILES,instance=estudante)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados alterados com sucesso")
            return HttpResponseRedirect(reverse('estudante:minha-conta'))

    context = {
        'estudante':estudante,
        'form':form,
        'totMatrivulados':MatriculaCurso.objects.all().filter(user = request.user, estado = True).count()
        }
    return render(request, 'estudante/minhaConta.html', context)


@login_required(login_url='accounts:user_login')
@allowed_users(allowed_roles=['estudante'])
def enviarDuvida(request, pk):
    # estadoMensagem = DuvidaAula.objects.all().filter(estadoVisto=False).count()
    videosObjecto = Video.objects.get(id = int(pk))
    objecto = Curso.objects.get(id = int(videosObjecto.curso.id))
    videos = Video.objects.all().filter(curso = objecto)

    objecto = DuvidaAula.objects.all()
    form = DuvidaAulaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            f1 = form.save(commit=False)
            f1.transmissor = request.user
            f1.receptor = User.objects.get(username = 'admin')
            f1.save()
            # return HttpResponseRedirect(reverse('estudante:chat-cliente'))
            messages.info(request, "Dúvida enviada")
            return HttpResponseRedirect(reverse('estudante:assistir-curso', kwargs={'pk':int(videosObjecto.id)}))

    user = request.user
    cliente = Estudante.objects.get(user = user)
    mensagens = Estudante.objects.all()
    mensagens.update(estadoVisto=True)
    args = {
        'mensagens':mensagens,
        'cliente':cliente,
        'form':form,
    }
    return render(request, 'estudante/assistirCurso.html', args)

@login_required(login_url='accounts:user_login')
@allowed_users(allowed_roles=['estudante'])
def perfilProfessor(request, pk):
    professor = Professor.objects.get(id = int(pk))
    cursosProfessor = Curso.objects.all().filter(user = professor.user)
    totCursos = cursosProfessor.count()
    totalAvaliacao = 0
    n1 = 0

    form = AvaliarProfessorForm(request.POST or None)

    try:
        objectoEstudante = AvaliarProfessor.objects.all().filter(estudante = request.user)

        n1 = objectoEstudante[0]

        if n1 is None:
            n1 = 0
        else:
            n1 = n1

        objectoAvaliacao = objectoEstudante.aggregate(theta=Sum('avaliacao'))

        if objectoAvaliacao['theta'] is not None:
            objectoAvaliacao['theta'] = objectoAvaliacao['theta']
        else:
            objectoAvaliacao['theta'] = 0

        totalAvaliacao = AvaliarProfessor.objects.all().aggregate(theta=Sum('avaliacao')) / AvaliarProfessor.objects.all().count()

        print(objectoAvaliacao['theta'])
        print(totalAvaliacao)


    except:
        objectoEstudante = 0

    if form.is_valid():
        f1 = form.save(commit=False)
        f1.professor = professor.user
        f1.estudante = request.user
        f1.save()
        return HttpResponseRedirect(reverse('estudante:perfil-professor', kwargs={'pk':int(professor.id)}))

    args = {
        'professor':professor,
        'cursosProfessor':cursosProfessor,
        'totCursos':totCursos,
        'form':form,
        'objectoEstudante':objectoEstudante,
        'totalAvaliacao':totalAvaliacao,
        'n1':n1
    }
    return render(request, 'estudante/perfilProfessor.html', args)


@login_required(login_url='accounts:user_login')
@allowed_users(allowed_roles=['cliente'])
def eliminarDuvida(request, pk):
    objecto = DuvidaAula.objects.get(id = int(pk))
    objecto.delete()
    messages.error(request, "Dúvida eliminada")
    return HttpResponseRedirect(reverse('estudante:assistir-curso', kwargs={'pk':int(objecto.aula.id)}))


@login_required(login_url='accounts:user_login')
@allowed_users(allowed_roles=['estudante'])
def reportarErro(request):
    form = ReportarErroForms(request.POST or None, files=request.FILES)
    if form.is_valid():
        f1 = form.save(commit=False)
        f1.user = request.user
        f1.save()
        return HttpResponseRedirect(reverse('estudante:sucesso-erro'))
    args = {
        'form':form
    }
    return render(request, 'estudante/reportar_erro.html', args)

@login_required(login_url='accounts:user_login')
@allowed_users(allowed_roles=['estudante'])
def sucessoErro(request):
    return render(request, 'estudante/sucesso_erro.html')

@login_required(login_url='accounts:user_login')
@allowed_users(allowed_roles=['estudante'])
def ajuda(request):
    user = request.user
    estudante = Estudante.objects.get(user = user)
    tipo_artigo = TipoArtigo.objects.all()
    args = {
        'tipo_artigo':tipo_artigo,'estudante':estudante
    }
    return render(request, 'estudante/ajuda.html', args)

@login_required(login_url='accounts:user_login')
@allowed_users(allowed_roles=['estudante'])
def artigos(request, pk):
    objecto = TipoArtigo.objects.get(id=int(pk))
    dados = Artigo.objects.all().filter(tipo_artigo=int(pk))
    paginacao = Paginator(dados, 12)
    pagina = request.GET.get('pagina')
    artigos = paginacao.get_page(pagina)
    args = {
        'artigos':artigos,
        'objecto':objecto
    }
    return render(request, 'estudante/artigos.html', args)

@login_required(login_url='accounts:user_login')
@allowed_users(allowed_roles=['estudante'])
def verArtigo(request, pk):
    objecto = Artigo.objects.get(id=int(pk))
    categoria = objecto.tipo_artigo
    artigos = Artigo.objects.all().filter(tipo_artigo=int(categoria.id))
    args = {
        'objecto':objecto,
        'categoria':categoria,
        'artigos':artigos,
    }
    return render(request, 'estudante/ver_artigo.html',args)