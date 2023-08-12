from django.db import models
from .matricula import Matricula
from .professor import Professor
from .aluno import Aluno
from datetime import date 


class Mensagem(models.Model):
    professor = models.ForeignKey(Professor)
    aluno = models.ForeignKey(Aluno)
    mensagem = models.TextField("Mensagem", blank=True)
    dt_envio = models.DateField("Data de envio", default=date(year=1900, month=1, day=1))