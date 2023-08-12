from django.db import models

from django.contrib.auth.models import User



class Coordenador(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuario')
    celular = models.CharField(max_length=20, verbose_name='Celular', blank=True)

    class Meta:
        verbose_name = 'Coordenador'
        verbose_name_plural = 'Coordenadores'
                                       
    def __str__(self):
        return self.usuario.first_name