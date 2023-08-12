from django.db import models
from .curso import Curso




class Disciplina(models.Model):
    nome = models.CharField('Disciplina', max_length=50, unique=True)
    curso = models.ManyToManyField(Curso)
    carga_horaria = models.IntegerField(verbose_name='Carga horaria')
    imagem = models.ImageField(upload_to='imagens/', blank=True)

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.nome