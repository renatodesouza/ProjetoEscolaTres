from django.db import models
from .curso import Curso
from .aluno import Aluno
from .turma import Turma




class Matricula(models.Model):
    ATIVA = 'ATV'
    CANCELADA = 'Canc'
    TRANCADA = 'Trc'
    EM_ANALISE = 'An'
    SOLICITADA = 'SO'

    escolha_situacao = [
        (ATIVA, 'Ativa'),
        (CANCELADA, 'Cancelada'),
        (TRANCADA, 'Trancada'),
        (EM_ANALISE, 'Em Analise'),
        (SOLICITADA, 'Solicitada')
        ]
    
    
    status = models.CharField(max_length=4, choices=escolha_situacao, default=None)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT, related_name='matricula')
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT, related_name='matricula')
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name='matricula')
    dt_inicio = models.DateField()
    dt_final = models.DateField()

    

    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'

    def __str__(self) -> str:
        return self.status