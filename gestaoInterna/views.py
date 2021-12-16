from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import *
from .forms import *
from professor.models import *
from estudante.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# gestao

@login_required(login_url='accounts:login-administracao')
def index(request):
    totEstudantes = Estudante.objects.all()
    totProfessor = Professor.objects.all()
    totCursos = Curso.objects.all()

    args = {
      'totEstudantes':totEstudantes.count(),
      'totProfessor':totProfessor.count(),
      'totCursos':totCursos.count()
    }
    return render(request, 'gestao/index.html', args)

def professoresGestao(request):
    User = get_user_model()

    dados = User.objects.all().filter(groups__name='professor')
    paginacao = Paginator(dados, 10)
    pagina = request.GET.get('pagina')
    users = paginacao.get_page(pagina)

    args = {
    'professor': Professor.objects.all(),
    'totCursos':Curso.objects.all().count(),
    'users':users
    }
    return render(request, 'gestao/professoresGestao.html', args)

def professoresGestaoDetalhes(request, pk):
    User = get_user_model()
    objecto = User.objects.get(id = int(pk))

    cursos = Curso.objects.all().filter(user = objecto)
    totalCursos = cursos.count()

    curriculo = CurriculoProfessor.objects.all().filter(user = objecto)

    professor = Professor.objects.get(user = objecto)
    args = {
        'objecto':objecto,
        'professor':professor,
        'cursos':cursos,
        'totalCursos':totalCursos,
        'curriculo':curriculo
    }
    return render(request, 'gestao/professoresGestaoDetalhes.html', args)

def cvProfessor(request, pk):
    User = get_user_model()
    objecto = User.objects.get(id = int(pk))

    curriculo = CurriculoProfessor.objects.all().filter(user = objecto)

    args = {
        'objecto':objecto,
        'curriculo':curriculo
    }

    return render(request, 'gestao/cvProfessor.html', args)

def professoresGestaoCursoDetalhes(request, pk):
    objecto = Curso.objects.get(id = int(pk))
    alunos = MatriculaCurso.objects.all().filter(curso = objecto)

    videos = Video.objects.all().filter(curso = objecto)
    totVideos = videos.count()
    args = {
        'videos':videos,
        'totVideos':totVideos,
        'alunos':alunos,
        'objecto':objecto
    }
    return render(request, 'gestao/professoresGestaoCursoDetalhes.html', args)

def estadoUser(request, pk):
    User = get_user_model()
    objecto = User.objects.get(id = int(pk))
    if objecto.is_active == True:
        objecto.is_active = False
    else:
        objecto.is_active = True
    objecto.save()
    return HttpResponseRedirect(reverse('gestaoInterna:professores-gestao-detalhes', kwargs={'pk':int(objecto.id)}))

   
def detahesCursoGestao(request, pk):
    videosObjecto = Video.objects.get(id = int(pk))
    objecto = Curso.objects.get(id = int(videosObjecto.curso.id))
    videos = Video.objects.all().filter(curso = objecto)

    professor = Professor.objects.filter(user = objecto.user)

    duvidas = DuvidaAula.objects.all().filter(aula = videosObjecto).order_by('-dataEnvio')
    totDuvidas = duvidas.count()

    args = {
        'objecto':objecto,
        'videos':videos,
        'videosObjecto':videosObjecto,
        'duvidas':duvidas,
        'professor':professor[0],
        'totDuvidas':totDuvidas
    }
    return render(request, 'gestao/assistirCurso.html', args)



@login_required(login_url='accounts:login-administracao')
def notificacoes(request):
    return render(request, 'gestao/reservas_gestao.html')

#+----------------------//magazine//--------------------+
@login_required(login_url='accounts:login-administracao')
def magazineGestao(request):

    dados = CategoriaMagazine.objects.all().order_by('-data_criacao')
    paginacao = Paginator(dados, 12)
    pagina = request.GET.get('pagina')
    categoria = paginacao.get_page(pagina)


    form = CategoriaMagazineForm(request.POST or None)
    if form.is_valid():
        f1 = form.save(commit = False)
        f1.user = request.user
        f1.save()
        messages.success(request, "Registo feito com sucesso")
        return HttpResponseRedirect('magazine-gestao')
    context = {
        'categoria':categoria,
        'form':form,
        'tot':CategoriaMagazine.objects.all().order_by('-data_criacao').count()
    }
    return render(request, 'gestao/magazine_gestao.html', context)

@login_required(login_url='accounts:login-administracao')
def magazineArtigos(request, pk):
    objecto = CategoriaMagazine.objects.get(id=int(pk))

    dados = Magazine.objects.all().filter(categoria=pk, estado='Activado').order_by('-data_criacao')
    paginacao = Paginator(dados, 12)
    pagina = request.GET.get('pagina')
    artigos = paginacao.get_page(pagina)

    artigosDesabilitados = Magazine.objects.all().filter(categoria=pk,estado='Desactivado').order_by('-data_criacao')

    form = MagazieForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        f1 = form.save(commit=False)
        f1.user = request.user
        f1.categoria = objecto
        f1.save()
        # return HttpResponseRedirect(reverse('gestaoInterna:magazine-gestao'))
        messages.success(request, "Artigo registado com sucesso")
        return HttpResponseRedirect(reverse('gestaoInterna:magazine-artigos', kwargs={'pk':int(objecto.id)}))
        # return HttpResponseRedirect(reverse('gestaoInterna:ajuda_artigos', kwargs={'pk': objecto}))
    context = {
        'artigos':artigos,
        'objecto':objecto,
        'form':form,
        'artigosDesabilitados':artigosDesabilitados,
        'tot':Magazine.objects.all().filter(categoria=pk,estado='Activado').order_by('-data_criacao').count()
    }
    return render(request, 'gestao/magazine_artigos.html', context)

def verArtigoMagazine(request, pk):
    objecto = Magazine.objects.get(id = int(pk))
    artigos = Magazine.objects.filter(categoria = objecto.categoria)
    args = {
        'objecto':objecto,
        'artigos':artigos,
    }
    return render(request, 'gestao/verArtigoMagazine.html', args)

@login_required(login_url='accounts:login-administracao')
def eliminarMagazine(request, pk):
    item = Magazine.objects.get(id=int(pk))
    if item.estado == 'Desactivado':
        item.estado = "Activado"
    else:
        item.estado = 'Desactivado'
    item.save()
    messages.info(request, "Estado alterado")
    return HttpResponseRedirect(reverse('gestaoInterna:magazine-artigos', kwargs={'pk':int(item.categoria.id)}))
    # return HttpResponseRedirect(reverse('gestaoInterna:magazine-gestao'))

def editarCategoriaMagazine(request, pk):
    objecto = CategoriaMagazine.objects.get(id = int(pk))
    form = CategoriaMagazineForm(instance=objecto)
    if request.POST:
        form = CategoriaMagazineForm(request.POST or None, instance=objecto)
        if form.is_valid():
            form.save()
            messages.success(request, "Alterações guardadas")
            return HttpResponseRedirect(reverse('gestaoInterna:magazine-gestao'))
    args = {
        'objecto':objecto,
        'form':form
    }
    return render(request, 'gestao/editarCategoriaMagazine.html', args)


@login_required(login_url='accounts:login-administracao')
def editar_magazine_artigos(request, pk):
    objecto = Magazine.objects.get(id=int(pk))
    form = MagazieForm(instance=objecto)
    if request.POST:
        form = MagazieForm(request.POST or None, instance=objecto, files=request.FILES)
        if form.is_valid():
            f1 = form.save(commit=False)
            f1.foto = objecto.foto
            f1.save()
            messages.success(request, "Alterações guardadas")
            return HttpResponseRedirect(reverse('gestaoInterna:ver-artigo-magazine', kwargs={'pk':int(objecto.id)}))

    context = {
        'objecto':objecto,
        'form':form
    }

    return render(request, 'gestao/editar_magazine_artigos.html', context)

#+----------------------/magazine/--------------------+

@login_required(login_url='accounts:login-administracao')
def ajudaGestao(request):
    tipo_artigo = TipoArtigo.objects.all()
    form = TipoArtigoForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        f1 = form.save(commit = False)
        f1.user = request.user
        f1.save()
        return HttpResponseRedirect('ajuda-gestao')
    context = {
        'tipo_artigo':tipo_artigo,
        'form':form,
    }
    return render(request, 'gestao/ajuda.html', context)

@login_required(login_url='accounts:login-administracao')
def ajudaArtigos(request, pk):
    objecto = TipoArtigo.objects.get(id=int(pk))
    artigos = Artigo.objects.all().filter(tipo_artigo=pk, estado=True)

    form = ArtigoForm(request.POST or None)
    if form.is_valid():
        f1 = form.save(commit=False)
        f1.user = request.user
        f1.tipo_artigo = objecto
        f1.save()
        return HttpResponseRedirect(reverse('gestaoInterna:ajuda-gestao'))
        # return HttpResponseRedirect(reverse('gestaoInterna:ajuda_artigos', kwargs={'pk': objecto}))
    context = {
        'artigos':artigos,
        'objecto':objecto,
        'form':form
    }
    return render(request, 'gestao/artigo.html', context)

@login_required(login_url='accounts:login-administracao')
def eliminarArtigo(request, pk):
    item = Artigo.objects.get(id=int(pk))
    form = ArtigoForm(request.POST or None, instance=item)
    if form.is_valid():
        f1 = form.save(commit=False)
        f1.estado = False
        f1.save()
        return HttpResponseRedirect(reverse('gestaoInterna:ajuda-gestao'))

    return render(request, 'gestao/eliminar_item.html', {'form':form, 'item':item})

# def add_tipo_artigo(request):
#     form = TipoArtigoForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     args = {
#         'form':form,
#         }
#     return render(request, 'gestao/add_tipo_artigo.html', args)

@login_required(login_url='accounts:login-administracao')
def errosReportados(request):
    dados = ReportarErro.objects.all().order_by('-data_criacao')
    paginacao = Paginator(dados, 12)
    pagina = request.GET.get('pagina')
    erros = paginacao.get_page(pagina)
    context = {
        'erros':erros
    }
    return render(request, 'gestao/erros_gestao.html', context)

def detalhesErro(request, pk):
    objecto = ReportarErro.objects.get(id = int(pk))
    context = {
        'objecto':objecto
    }
    return render(request, 'gestao/erros_detalhes.html', context)

@login_required(login_url='accounts:login-administracao')
def editar_ajuda_artigos(request, pk):
    objecto = Artigo.objects.get(id=int(pk))
    form = ArtigoForm(request.POST or None, instance=objecto)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('gestaoInterna:ajuda-gestao'))

    context = {
        'objecto':objecto,
        'form':form
    }

    return render(request, 'gestao/editar_ajuda_artigos.html', context)

def verArtigoAjuda(request, pk):
    objecto = Artigo.objects.get(id=int(pk))
    categoria = objecto.tipo_artigo
    artigos = Artigo.objects.all().filter(tipo_artigo=int(categoria.id))
    args = {
        'objecto':objecto,
        'categoria':categoria,
        'artigos':artigos,
    }
    return render(request, 'gestao/ver_artigo.html',args)

#+----------------------//Gestao Usuarios//--------------------+

@login_required(login_url='accounts:login-administracao')
def gestaoConta(request):    
    return render(request, 'gestao/gestao_users.html')

@login_required(login_url='accounts:login-administracao')
def ativar_desativar_conta(request,pk):
    user = User.objects.get(pk = int(pk))
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('gestaoInterna:gestao_conta'))

@login_required(login_url='accounts:login-administracao')
def cadastar_gestao(request):
    context = {}
    return render(request, 'gestao/gestao_users.html', context)

@login_required(login_url='accounts:login-administracao')
def login_gestao(request):
    context = {}
    return render(request, 'gestao/gestao_users.html', context)

def gestao(request):
    return render(request, 'gestao/gestao.html')

def estudantesGestao(request):
    User = get_user_model()

    dados = User.objects.all().filter(groups__name='estudante')
    paginacao = Paginator(dados, 10)
    pagina = request.GET.get('pagina')
    users = paginacao.get_page(pagina)

    args = {
    'estudantes': Estudante.objects.all(),
    'users':users
    }
    return render(request, 'gestao/estudantesGestao.html', args)

def estudantesGestaoDetalhes(request, pk):
    User = get_user_model()
    objecto = User.objects.get(id = int(pk))

    estudante = Estudante.objects.get(user = objecto)
    args = {
        'objecto':objecto,
        'estudante':estudante,
       
    }
    return render(request, 'gestao/estudantesGestaoDetalhes.html', args)