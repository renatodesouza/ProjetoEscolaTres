from django.db import models
from django.contrib.auth.models import User
from .disciplina import Disciplina



class Professor(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='professor', verbose_name='Usuario')
    celular = models.CharField('Celular', max_length=20)
    disciplina = models.ManyToManyField(Disciplina, blank=True, related_name='professor')
                                       
    def __str__(self):
        return self.usuario.username