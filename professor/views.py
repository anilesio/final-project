from django.contrib.auth.decorators import login_required
from django.forms.forms import Form
from django.shortcuts import render, HttpResponseRedirect, reverse
from accounts.decorators import *
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import *
from .models import *
from gestaoInterna.models import *
from gestaoInterna.forms import ReportarErroForms
from estudante.models import MatriculaCurso, Estudante

@login_required(login_url='accounts:user-login')
@allowed_users(allowed_roles=['professor'])
def index(request):
    cursos = Curso.objects.all()
    totalCursos = cursos.count()

    args = {
        'cursos':cursos,
        'totalCursos':totalCursos
    }
    return render(request, 'professor/index.html', args)

@login_required(login_url='accounts:user-login')
@allowed_users(allowed_roles=['professor'])
def novoCurso(request):
    form = CursoFrom(request.POST or None)
    try:
        if form.is_valid():
            f1 = form.save(commit=False)
            f1.user = request.user
            f1.save()
            messages.success(request, "Curso publicado com successo")
            messages.info(request, "Ainda falta um passo")
            messages.info(request, "Adicone aulas ao seu novo curso")
            return HttpResponseRedirect(reverse('professor:meus-cursos'))
    except:
        messages.success(request, "Erro no registo")
        return HttpResponseRedirect(reverse('professor:meus-cursos'))
    args = {
        'form':form
    }
    return render(request, 'professor/novoCurso.html', args)

def meusCursos(request):
    cursos = Curso.objects.all().filter(user = request.user)
    totalCursos = cursos.count()

    args = {
        'cursos':cursos,
        'totalCursos':totalCursos
    }
    return render(request, 'professor/meusCursos.html', args)

def detalhesCurso(request, pk):
    objecto = Curso.objects.get(id = int(pk))
    alunos = MatriculaCurso.objects.all().filter(curso = objecto)

    form = VideoFrom(request.POST or None, files=request.FILES)

    if form.is_valid():
        f1 = form.save(commit=False)
        f1.curso = objecto
        f1.save()
        messages.success(request, "Aula registada")
        return HttpResponseRedirect(reverse('professor:detalhes-curso', kwargs={'pk':int(objecto.id)}))

    videos = Video.objects.all().filter(curso = objecto)
    totVideos = videos.count()

    args = {
        'objecto':objecto,
        'videos':videos,
        'totVideos':totVideos,
        'form':form,
        'alunos':alunos,
        'matrilados':alunos.count()
    }
    return render(request, 'professor/detalhesCurso.html', args)

def detalhesVideo(request, pk):
    objecto = Video.objects.get(id = int(pk))
    outrosVideos = Video.objects.all().filter(curso = objecto.curso)
    form = VideoFrom(instance=objecto)
    if request.POST:
        form = VideoFrom(request.POST or None, files=request.FILES, instance=objecto)
        if form.is_valid():
            f1 = form.save(commit=False)
            f1.video = objecto.video
            f1.save()
            messages.success(request, "Alterações guardadas")
            return HttpResponseRedirect(reverse('professor:detalhes-video', kwargs={'pk':int(objecto.curso.id)}))
    args = {
        'objecto':objecto,
        'outrosVideos':outrosVideos,
        'form':form
    }
    return render(request, 'professor/detalhesVideo.html', args)

def eliminarVideo(request, pk):
    objecto = Video.objects.get(id = int(pk))
    objecto.delete()
    messages.error(request, "Vídeo eliminado")
    return HttpResponseRedirect(reverse('professor:detalhes-curso', kwargs={'pk':int(objecto.curso.id)}))

def avisoCurso(request, pk):
    objecto = Curso.objects.get(id = int(pk))
    totVideos = Video.objects.all().filter(curso = objecto).count()
    matrilados = MatriculaCurso.objects.all().filter(curso = objecto).count()
    args = {
        'objecto':objecto,
        'totVideos':totVideos,
        'matrilados':matrilados
    }
    return render(request, 'professor/avisoCurso.html', args)

def eliminarCurso(request, pk):
    objecto = Curso.objects.get(id = int(pk))
    objecto.delete()
    messages.error(request, "Curso eliminado")
    return HttpResponseRedirect(reverse('professor:meus-cursos'))

def perfilEstudante(request):
    user = request.user
    estudante = Estudante.objects.get(user = user)

    context = {
        'estudante':estudante,
        'totMatrivulados':MatriculaCurso.objects.all().filter(user = request.user, estado = True).count()
        }
    return render(request, 'professor/perfilEstudante.html', context)


@login_required(login_url='accounts:user_login')
@allowed_users(allowed_roles=['professor'])
def reportarErro(request):
    form = ReportarErroForms(request.POST or None, files=request.FILES)
    if form.is_valid():
        f1 = form.save(commit=False)
        f1.user = request.user
        f1.save()
        return HttpResponseRedirect(reverse('professor:sucesso-erro'))
    args = {
        'form':form
    }
    return render(request, 'professor/reportar_erro.html', args)

@login_required(login_url='accounts:user_login')
@allowed_users(allowed_roles=['professor'])
def sucessoErro(request):
    return render(request, 'professor/sucesso_erro.html')

@login_required(login_url='accounts:user_login')
@allowed_users(allowed_roles=['professor'])
def ajuda(request):
    user = request.user
    professor = Professor.objects.get(user = user)
    tipo_artigo = TipoArtigo.objects.all()
    args = {
        'tipo_artigo':tipo_artigo,'professor':professor
    }
    return render(request, 'professor/ajuda.html', args)

@login_required(login_url='accounts:user_login')
@allowed_users(allowed_roles=['professor'])
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
    return render(request, 'professor/artigos.html', args)

@login_required(login_url='accounts:user_login')
@allowed_users(allowed_roles=['professor'])
def verArtigo(request, pk):
    objecto = Artigo.objects.get(id=int(pk))
    categoria = objecto.tipo_artigo
    artigos = Artigo.objects.all().filter(tipo_artigo=int(categoria.id))
    args = {
        'objecto':objecto,
        'categoria':categoria,
        'artigos':artigos,
    }
    return render(request, 'professor/ver_artigo.html',args)

def turmas(request):

    dados = Turma.objects.all()
    paginacao = Paginator(dados, 12)
    pagina = request.GET.get('pagina')
    turmas = paginacao.get_page(pagina)

    form = TurmaFrom(request.POST or None)
    if form.is_valid():
        f1 = form(commit=False).save
        f1.user = request.user
        f1.save()
        messages.success(request, "Turma registada com sucesso")
        return HttpResponseRedirect(reverse('professor:turmas'))
    args = {
    'turmas':turmas,
    'form':form
    }
    return render(request, 'professor/turmas.html', args)
