from django.db import models
from .matricula import Matricula
from .professor import Professor
from .aluno import Aluno
from django.contrib.auth.models import User
from datetime import date 


class Mensagem(models.Model):
    remetente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens_recebidas')
    assunto = models.CharField(max_length=200, blank=True)
    mensagem = models.TextField("Mensagem", blank=True)
    
    dt_envio = models.DateField("Data de envio", default=date(year=1900, month=1, day=1))