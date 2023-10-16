# Generated by Django 3.2 on 2023-10-15 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_mensagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='periodo',
            field=models.CharField(choices=[('Matutino', 'Matutino'), ('Noturno', 'Noturno')], default='MATUTINO', max_length=20),
        ),
        migrations.AlterField(
            model_name='entregaatividade',
            name='atividade',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='atividade_entregue', to='app.atividade'),
        ),
    ]
