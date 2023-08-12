from django.db import models
from .coordenador import Coordenador


class Curso(models.Model):

    MATUTINO = 'MATUTINO'
    NOTURNO = 'NOTURNO'

    escolha_periodo = [
        (MATUTINO, 'MATUTINO'),
        (NOTURNO, 'NOTURNO')
    ]

    PRESENCIAL = 'PRESENCIAL'
    ONLINE = 'ONLINE'

    escolha_modalidade = [
        (PRESENCIAL, 'PRESENCIAL'),
        (ONLINE, 'ONLINE')
    ]

    nome = models.CharField(max_length=30, verbose_name='Nome')
    descricao = models.TextField(max_length=500, default=None, verbose_name='Descricao')
    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT, related_name='cursos')
    periodo = models.CharField(max_length=20, choices=escolha_periodo, default='MATUTINO')
    modalidade = models.CharField(max_length=20, choices=escolha_modalidade, default='PRESENCIAL')
    imagem = models.ImageField(upload_to='imagens/', blank=True)

    def __str__(self):
        return self.nome