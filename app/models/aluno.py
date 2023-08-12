from django.db import models

from django.contrib.auth.models import User
from datetime import date

    

class Aluno(models.Model):
    ra = models.CharField(max_length=10, unique=True, verbose_name='RA')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    data_expiracao = models.DateField('Data de Expiracao', default=date(year=1900, month=1, day=1))
    imagem = models.ImageField("Imagem", upload_to='imagens/', blank=True)
                                       
    def __str__(self):
        return self.usuario.username