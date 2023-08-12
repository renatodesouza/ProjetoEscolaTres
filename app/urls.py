from django.urls import path
from . import views
from .views import HomeView, CursoView, AlunoView, create, delete,cursos, login, usuario
from django.views.generic import TemplateView



app_name = 'app'

urlpatterns = [
    # path('home/', views.index, name='index'),
    # path('curso/<int:pk>/', views.curso, name='curso'),
    path('home/', HomeView.as_view(), name='index'),
    path('curso/<int:pk>/', CursoView.as_view(), name='curso'),
    path('aluno/<int:pk>/', AlunoView.as_view(), name='aluno'),
    path('cursos/', views.cursos, name='cursos'),

    path('curso-create/', views.create , name='create'),
    path('curso-delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
    
    path('login/', views.login, name='login'),
    path('usuario/', views.usuario, name='usuario'),
]