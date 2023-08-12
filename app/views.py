
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import default_storage
from django.views.generic import DetailView, TemplateView
from .models.curso import Curso
from .models.turma import Turma
from .models.aluno import Aluno
from .models.matricula import Matricula
from .models.atividade import Atividade
from app.models.coordenador import Coordenador

from .forms import CursoForm, LoginForm


def index(request):
    cursos = Curso.objects.all().order_by('?')
    return render(request, 'app/index.html', context={'cursos':cursos})


def curso(request, pk):
    cursos = Curso.objects.all()

    curso = Curso.objects.get(pk=pk)
    
    turmas = Turma.objects.filter(curso__nome=curso).filter(turma='TURMA A')

    disciplinas_por_semestre = []

    for turma in turmas:
        semestre = turma.semestre
        
        disciplinas = turma.disciplina.all()

        disciplinas_por_semestre.append({
            'semestre':semestre,
            'disciplinas':disciplinas
        })
        print('-----------------------------------------------------------------------------------')
        print(curso)
        print(turma)
        print(semestre)
        print(disciplinas_por_semestre)
        print('-----------------------------------------------------------------------------------')

        context = {
            'curso':curso,
            'disciplinas_por_semestre': disciplinas_por_semestre,
            'cursos':cursos
    }
    
        
    return render(request, 'app/curso.html', context)


# ------------------------------------------------------------------


class HomeView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.order_by('?')[:3]

        return context
    

class CursoView(DetailView):
    template_name = 'app/curso.html'
    model = Curso
    context_object_name = 'curso'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()
        curso = self.get_object()
        turmas = Turma.objects.filter(curso__nome=curso, turma='TURMA A')

        disciplinas_por_semestre = [
            {'semestre':turma.semestre,
             'disciplinas':turma.disciplina.all()}
             for turma in turmas
        ]

        context['disciplinas_por_semestre'] = disciplinas_por_semestre

        return context

class AlunoView(DetailView):
    template_name = 'app/aluno.html'
    model = Aluno
    context_object_name = 'aluno'
    
    def get_queryset(self):
        self.nome = get_object_or_404(Aluno, pk=self.kwargs['pk'])
        return Aluno.objects.filter(id=self.nome.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        aluno = self.get_object()

        matricula = Matricula.objects.get(aluno=aluno)
        cursos = Curso.objects.all()
        
        context['turma'] = matricula.turma
        context['curso'] = matricula.curso
        context['cursos'] = cursos
        context['disciplinas'] = matricula.turma.disciplina.all()
        context['atividades'] = matricula.turma.atividades.all()
        context['atividades_limit'] = matricula.turma.atividades.order_by('?')[:2]
        
        return context



def create(request):

    cursos = Curso.objects.all()

    coordenadores = Coordenador.objects.all()

    context = {
        'cursos':cursos,
        'coordenadores':coordenadores
        }

    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        periodo = request.POST.get('periodo')
        modalidade = request.POST.get('modalidade')
        imagem = request.FILES.get('imagem')

        coordenador_id = request.POST.get('coordenador')

        coordenador = get_object_or_404(Coordenador, pk=coordenador_id)

        if imagem:
            caminho_imagem = default_storage.save(imagem.name, imagem)
            print(caminho_imagem)

        Curso.objects.create(nome=nome, descricao=descricao, coordenador=coordenador, periodo=periodo, modalidade=modalidade, imagem=caminho_imagem)

        return redirect('app:cursos')
    return render(request, 'app/curso_create.html', context)


def update(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    
    coordenadores = Coordenador.objects.all()
    context = {'curso':curso, 'coordenadores':coordenadores}
    print(request.method)
    if request.method == 'POST':
        
        curso.nome = request.POST.get('nome')
        curso.descricao = request.POST.get('descricao')
        curso.periodo = request.POST.get('periodo')
        curso.modalidade = request.POST.get('modalidade')

        coordenador_id = request.POST.get('coordenador')

        coordenador = get_object_or_404(Coordenador, pk=coordenador_id)
        curso.coordenador = coordenador

        if 'imagem' in request.FILES:
            curso.imagem = request.FILES['imagem']      

        curso.save()

        return redirect('app:cursos')
   
    return render(request, 'app/curso_edita.html', context=context)
    

def delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return redirect('app:cursos')
    
   
def cursos(request):
    cursos = Curso.objects.all()
    context = {'cursos':cursos}
    return render(request, 'app/cursos.html', context=context)


def login(request):
    forms = LoginForm()
    context = {'forms':forms}

    return render(request, 'app/login.html', context)

def usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        context = {'form':form}
        return render(request, 'app/usuario.html', context)