from typing import Any, List, Optional, Tuple, Union
from django.contrib import admin
from django.db.models.query import Q, QuerySet

from django.http.request import HttpRequest
from .models.atividade import Atividade
from .models.aluno import Aluno
from .models.coordenador import Coordenador
from .models.curso import Curso
from .models.disciplina import Disciplina
from .models.matricula import Matricula
from .models.professor import Professor
from .models.turma import Turma
from .models.entrega_atividade import EntregaAtividade

from django.contrib.auth.models import Group

from .forms import AtividadeForm



@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):

    list_display = ('id', 'ra', 'usuario', 'data_expiracao', 'imagem')

    fieldsets = [
        ('Informações do Aluno',        {'fields':('ra', 'usuario', 'data_expiracao', 'imagem')})
    ]

    search_fields = ['ra']



@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'descricao', 'status', 'atividade',
                    'dt_inicio', 'dt_fim', 'professor', 'disciplina')
    
    fieldsets = [
        ('Atividade',           {'fields':('titulo', 'descricao', 'atividade', 'status')}),
        ('Professor',           {'fields':('professor',)}),
        ('Disciplina',          {'fields':('disciplina',)}),
        ('Turmas',              {'fields':('turma',)}),
        ('Datas',               {'fields':('dt_inicio', 'dt_fim')})
    ]


    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        
        return queryset.filter(professor__usuario=request.user) or queryset.filter(turma__matricula__aluno__usuario=request.user)


@admin.register(Coordenador)
class CoordenadorAdmin(admin.ModelAdmin):

    list_display = ('usuario', 'celular')

    fieldsets = [
        ("Informoções do Coordenador",        {'fields': ('usuario', 'celular')})
    ]

    search_fields = ['usuario']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):

    list_display = ('id', 'nome', 'descricao', 'periodo', 'modalidade', 'coordenador', 'imagem')

    fieldsets = [
    ('Informações basicas',             {'fields': ('nome', 'descricao')}),
    ('Horarios',                        {'fields': ('periodo', 'modalidade')}),
    ('Coordenador responsavel',         {'fields':('coordenador',)}),
    ('Imagem',                          {'fields':('imagem',)})
    ]
    
    search_fields = ['nome'] 


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')

    fieldsets = [
        ('Informações da Disciplina',   {'fields':('nome', 'carga_horaria')}),
        ('Cursos',               {'fields':('curso',)}),
        ('Imagem',                      {'fields':('imagem',)})
    ]

    search_fields = ['nome']
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(turma__matricula__aluno__usuario=request.user) or queryset.filter(professor__usuario=request.user)


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'turma', 'dt_inicio', 'dt_final', 'status')

    fieldsets = [
        ('Informações da matricula',            {'fields':('aluno', 'curso', 'turma',
                                                           'dt_inicio', 'dt_final', 'status')}),
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        print(queryset)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(aluno__usuario=request.user)

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):

    list_display = ('usuario', 'celular')

    fieldsets = [
        ("Informoções do Professor",        {'fields': ('usuario', 'celular')}),
        ("Disciplinas lecionadas",          {'fields':('disciplina',)})
    ]

    search_fields = ['usuario']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(usuario=request.user) 

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('turma', 'curso', 'semestre')

    fieldsets = [
        ('Informações da turma',       {'fields':('curso', 'turma', 'semestre', 'disciplina')}),
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(disciplina__professor__usuario=request.user) or queryset.filter(matricula__aluno__usuario=request.user)

@admin.register(EntregaAtividade)
class EntregaAtividadeAdmin(admin.ModelAdmin):

    list_display = ('atividade', 'aluno', 'professor', 'dt_entrega', 'status',
                    'nota', 'observacao', 'file')
    
    fieldsets = [
        ('Atividade',                       {'fields':('atividade',)}),
        ('Professor',                       {'fields':('professor',)}),
        ('Aluno',                           {'fields':('aluno',)}),
        ('Informações da Atividade',        {'fields':('status', 'resposta', 'file', 'nota')}),
        ('Observação',                      {'fields':('observacao',)})
    ]

    search_fields = ['aluno__usuario__first_name', 'atividade__nome', 'status', 'dt_entrega']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(aluno__usuario=request.user) or queryset.filter(professor__usuario=request.user)
        

    def get_readonly_fields(self, request, obj):
        campos_alunos = ('nota', 'status', 'titulo', 'observacao')
        campos_professores = ('aluno', 'resposta', 'file')

        grupos_aluno = Group.objects.filter(name='Alunos').exists()
        grupos_professor = Group.objects.filter(name='Professores').exists()
        grupos_coordenadores = Group.objects.filter(name='Coordenadores').exists()

        if grupos_aluno or grupos_professor or grupos_coordenadores:
            if obj or not obj:
                if grupos_aluno and request.user.groups.filter(name='Alunos').exists():
                    return campos_alunos

                if grupos_professor and (request.user.groups.filter(name='Professores').exists() or request.user.groups.filter(name='Coordenadores').exists()):
                    return campos_professores

        return self.readonly_fields    

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'aluno':
            print(request.user)
            kwargs['initial'] = request.user  # Define o valor inicial como o objeto aluno da requisição
            kwargs['disabled'] = False  # Desabilita a edição do campo pelo usuário
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    




    
    