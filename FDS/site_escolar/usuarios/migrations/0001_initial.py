# Generated by Django 5.1.1 on 2024-09-21 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=20, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('tipo_usuario', models.CharField(choices=[('aluno', 'Aluno'), ('professor', 'Professor')], max_length=9)),
            ],
        ),
    ]
