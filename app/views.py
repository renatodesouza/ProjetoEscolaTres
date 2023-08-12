
from typing import Any, Dict
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.views.generic import DetailView, TemplateView, CreateView
from .models.curso import Curso
from .models.turma import Turma
from .models.aluno import Aluno
from .models.professor import Professor
from .models.matricula import Matricula
from .models.atividade import Atividade
from app.models.coordenador import Coordenador
from django.urls import reverse_lazy
from .forms import CursoForm, LoginForm


def index(request):
    cursos = Curso.objects.all().order_by('?')
    return render(request, 'app/home.html', context={'cursos':cursos})


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
    template_name = 'app/home.html'

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
    context_object_name = 'user'
    
    def get_queryset(self):
        self.nome = get_object_or_404(Aluno, pk=self.kwargs['pk'])
        return Aluno.objects.filter(id=self.nome.id)

    def get_context_data(self, **kwargs):
        aluno = self.get_object()
        cursos = Curso.objects.all()
        matricula = Matricula.objects.get(aluno=aluno)
    
        context = super().get_context_data(**kwargs)
        context['cursos'] = cursos
        context['turma'] = matricula.turma
        context['curso'] = matricula.curso
        context['disciplinas'] = matricula.turma.disciplina.all()
        context['atividades'] = matricula.turma.atividades.all()
        context['atividades_limit'] = matricula.turma.atividades.order_by('?')[:2]
        
        return context

class ProfessorView(DetailView):
    template_name = 'app/professor.html'
    model = Professor
    context_object_name = 'user'

    def get_queryset(self):
        self.nome = get_object_or_404(User, pk=self.kwargs['pk'])
        return User.objects.filter(id=self.nome.id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
    
    if request.method == 'POST':
        nome = request.POST.get('usuario')
        pswd = request.POST.get('pswd')
        user = auth.authenticate(request, username=nome, password=pswd)
        print(user.id)
    
        if user is not None:
            auth.login(request, user)
            if user.is_staff:
                return redirect('app:professor', user.id)
            return redirect('app:aluno', user.id)
        return redirect('app:home')
    
    return render(request, 'app/login.html')




def login_dois(request):
    return render(request, 'app/login.html')


def logout(request):
    auth.logout(request)
    return redirect('app:login_dois')

def usuario_n(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        context = {'form':form}
        return render(request, 'app/usuario.html', context)
    

#---------------------------------------------------------------------------------------
class CursoCreateViews(CreateView):
    model = Curso
    form_class = CursoForm
   
    template_name = 'app/curso_create.html'
    success_url = reverse_lazy('app:cursos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['coordenadores'] = Coordenador.objects.all()
        return context