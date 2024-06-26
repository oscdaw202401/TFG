# Generated by Django 5.0.6 on 2024-06-01 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plazeduca', '0011_notas_id_alter_notas_dni_alumno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notas',
            name='id',
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='faltas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faltas', to='Plazeduca.asistencias'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='retrasos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retrasos', to='Plazeduca.asistencias'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='examen',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
