# Generated by Django 5.1.1 on 2024-11-03 19:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_avisoacademico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=20)),
                ('hora_inicio', models.TimeField()),
                ('hora_fim', models.TimeField()),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horarios', to='usuarios.materia')),
            ],
        ),
    ]