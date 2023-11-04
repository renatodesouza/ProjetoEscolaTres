from django.urls import path
from . import views
from .views import HomeView, CursoView, AlunoView, ProfessorView, CursoCreateView,\
create, delete,cursos, my_login, my_logout, boletim, cria_entrega_atividade
from django.views.generic import TemplateView



app_name = 'app'

urlpatterns = [
    
    path('home/', HomeView.as_view(), name='home'),
    path('curso/<int:pk>/', CursoView.as_view(), name='curso'),
    path('aluno/<int:pk>/', AlunoView.as_view(), name='aluno'),
    path('professor/<int:pk>/', ProfessorView.as_view(), name='professor'),
    
    path('boletim-aluno/', views.boletim, name='boletim'),
    path('cursos/', views.cursos, name='cursos'),

    path('curso-create/', CursoCreateView.as_view(), name='create'),
    path('curso-delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
    
    path('login/', views.my_login, name='my_login'),
    #path('curso-form/', CursoCreateView.as_view(), name='curso_form_create'),
    
    path('logout/', views.my_logout, name='my_logout'),

    path('cria-entrega-atividade/', view=cria_entrega_atividade, name='cria_entrega_atividade'),

    
]