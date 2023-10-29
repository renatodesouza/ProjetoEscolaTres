from django.db import models
from .atividade import Atividade
from .aluno import Aluno
from .professor import Professor
from datetime import datetime


class EntregaAtividade(models.Model):
    ENTREGUE = 'ENT'
    CORRIGIDO = 'COR'
    PENDENTE = 'PEN'

    escolha_status = [(ENTREGUE, 'Entregue'), (CORRIGIDO, 'Corrigido'), (PENDENTE, 'Pendente')]

    
    resposta = models.TextField(max_length=255, blank=True)
    status = models.CharField(max_length=3, choices=escolha_status, default=PENDENTE)
    nota = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT, related_name='entregas')
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    dt_entrega = models.DateField(auto_now=datetime.now())
    observacao = models.TextField(max_length=255)
    file = models.FileField(upload_to='file', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Entrega da Atividade' 

    def __str__(self):
        return f'Entrega da atividade {self.atividade} por {self.aluno}'
    


