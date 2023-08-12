from django.urls import path
from . import views
from .views import HomeView, CursoView, AlunoView, ProfessorView, create, delete,cursos, login, logout, login_dois
from django.views.generic import TemplateView



app_name = 'app'

urlpatterns = [
    # path('home/', views.index, name='index'),
    # path('curso/<int:pk>/', views.curso, name='curso'),
    path('home/', HomeView.as_view(), name='home'),
    path('curso/<int:pk>/', CursoView.as_view(), name='curso'),
    path('aluno/<int:pk>/', AlunoView.as_view(), name='aluno'),
    path('professor/<int:pk>/', ProfessorView.as_view(), name='professor'),
    path('cursos/', views.cursos, name='cursos'),

    path('curso-create/', views.create , name='create'),
    path('curso-delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
    
    path('login/', views.login, name='login'),
    path('login/', views.login_dois, name='login_dois'),
    
    path('logout/', views.logout, name='logout'),

    
]