from django.shortcuts import render
from professor.models import Curso, Professor
from django.core.paginator import Paginator
from gestaoInterna.models import *


# Create your views here.
def index(request):
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
    return render(request, 'publico/index.html', args)

def categorias(request):
    return render(request, 'publico/categorias.html')

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
    return render(request, 'publico/cursos.html', args)

def cursosFaculdade(request):
    return render(request, 'publico/cursosFaculdade.html')

def sejaProfessor(request):
    return render(request, 'publico/sejaProfessor.html')

def detalhesCurso(request, pk):
    objecto = Curso.objects.get(id = int(pk))

    professor = Professor.objects.get(user = objecto.user)

    dados = Curso.objects.all()
    paginacao = Paginator(dados, 10)
    pagina = request.GET.get('pagina')
    cursos = paginacao.get_page(pagina)

    args = {
        'cursos':cursos,
        'dados':dados,
        'professor':professor,
        'objecto':objecto
    }
    return render(request, 'publico/detalhesCurso.html', args)

def perfilProfessor(request, pk):
    professor = Professor.objects.get(id = int(pk))
    cursosProfessor = Curso.objects.all().filter(user = professor.user)
    totCursos = cursosProfessor.count()

    args = {
        'professor':professor,
        'cursosProfessor':cursosProfessor,
        'totCursos':totCursos,
    }
    return render(request, 'publico/perfilProfessor.html', args)


def ajuda(request):
    tipo_artigo = TipoArtigo.objects.all()
    args = {
        'tipo_artigo':tipo_artigo,
    }
    return render(request, 'publico/ajuda.html', args)

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
    return render(request, 'publico/artigos.html', args)

def ver_artigo(request, pk):
    objecto = Artigo.objects.get(id=int(pk))
    categoria = objecto.tipo_artigo
    artigos = Artigo.objects.all().filter(tipo_artigo=int(categoria.id))
    args = {
        'objecto':objecto,
        'categoria':categoria,
        'artigos':artigos,
    }
    return render(request, 'publico/ver_artigo.html',args)

def faqs(request):
    return render(request, 'publico/faq.html')

def magazine(request):
    categorias = CategoriaMagazine.objects.all().order_by('titulo').filter(estado=True)
    dados = Magazine.objects.all().order_by('-data_criacao').filter(estado='Activado')
    paginacao = Paginator(dados, 12)
    pagina = request.GET.get('pagina')
    artigos = paginacao.get_page(pagina)

    args = {
        'artigos':artigos,
        'categorias':categorias,
    }
    return render(request, 'publico/magazine.html', args)

def magazine_categorias(request, pk):
    categorias = CategoriaMagazine.objects.all()
    categoria = CategoriaMagazine.objects.get(id=int(pk))
    artigos = Magazine.objects.all().filter(categoria=int(categoria.id)).order_by('-data_criacao')
    args = {
        'categoria':categoria,
        'categorias':categorias,
        'artigos':artigos,
    }
    return render(request, 'publico/magazine_categorias.html', args)

def ver_magazine(request, pk):
    objecto = Magazine.objects.get(id=int(pk))
    categoria = objecto.categoria
    artigos = Magazine.objects.all().filter(categoria=int(categoria.id))
    args = {
        'objecto':objecto,
        'artigos':artigos,
        'categoria':categoria,
    }
    return render(request, 'publico/ver_magazine.html', args)

def estatisticas(request):
    return render(request, 'publico/estatisticas.html')

def politicaUso(request):
    return render(request, 'publico/politicaUso.html')