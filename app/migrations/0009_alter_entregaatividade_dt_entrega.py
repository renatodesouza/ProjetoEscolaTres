# Generated by Django 3.2 on 2023-06-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_entregaatividade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregaatividade',
            name='dt_entrega',
            field=models.DateField(auto_now=True),
        ),
    ]
