from django.db import models
from django.db.models import UniqueConstraint
from .disciplina import Disciplina
from .curso import Curso



class Turma(models.Model):
    A = 'TURMA A'
    B = 'TURMA B'
    C = 'TURMA C'
    D = 'TURMA D'

    escolha_turma = [
        (A, 'TURMA A'), 
        (B, 'TURMA B'), 
        (C, 'TURMA C'), 
        (D, 'TURMA D')
    ]

    PRIMEIRO_SEMESTRE = '1° SEMESTRE'
    SEGUNDO_SEMESTRE = '2° SEMESTRE'
    TERCEIRO_SEMESTRE = '3° SEMESTRE'
    QUARTO_SEMESTRE = '4° SEMESTRE'

    escolha_semestre = [(PRIMEIRO_SEMESTRE, 'PRIMEIRO SEMESTRE'), 
                        (SEGUNDO_SEMESTRE, 'SEGUNDO SEMESTRE'),
    			        (TERCEIRO_SEMESTRE, 'TERCEIRO SEMESTRE'), 
                        (QUARTO_SEMESTRE, 'QUARTO SEMESTRE')]

    turma = models.CharField("Turma", max_length=7, choices=escolha_turma, default=None)
    disciplina = models.ManyToManyField(Disciplina)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name='turmas')
    semestre = models.CharField(max_length=20, choices=escolha_semestre, default=PRIMEIRO_SEMESTRE)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

        constraints = [
            UniqueConstraint(fields=['turma', 'curso', 'semestre'], name='unique_turma',)
        ]

        

    def __str__(self):
        return f'{self.turma} | {self.semestre} | {self.curso}'