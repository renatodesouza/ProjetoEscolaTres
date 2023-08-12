from django.db import models
from datetime import date
from .disciplina import Disciplina
from .professor import Professor
from .turma import Turma



class Atividade(models.Model):
    ABERTA = 'ABERTA'
    FECHADA = 'FECHADA'
    PRORROGADA = 'PRORROGADA'
    
    escolha_status = [
                    (ABERTA, 'Aberta'),
                    (FECHADA, 'Fechada'),
                    (PRORROGADA, 'Prorrogada'),]
    
    ATV1 = 'ATV1'
    ATV2 = 'ATV2'
    ATV3 = 'ATV3'
    ATV4 = 'ATV4'
    ATV5 = 'ATV5'

    escolha_atividade = [(ATV1, 'ATV1'),
                         (ATV2, 'ATV2'),
                         (ATV3, 'ATV3'),
                         (ATV4, 'ATV4'),
                         (ATV5, 'ATV5')]
    
    titulo = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(max_length=255)
    status = models.CharField(max_length=10, choices=escolha_status)
    atividade = models.CharField('Atividade Complementar', max_length=4, choices=escolha_atividade, default=ATV1)

    dt_inicio = models.DateField('Data Inicio', default=date(year=1900, month=1, day=1))
    dt_fim = models.DateField('Data Fim', default=date(year=1900, month=1, day=1))

    professor = models.ForeignKey(Professor, on_delete=models.PROTECT, related_name='atividades')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, related_name='atividades')
    turma = models.ManyToManyField(Turma, blank=True, related_name='atividades')

    

    class Meta:
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.titulo