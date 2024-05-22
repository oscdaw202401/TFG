# Generated by Django 4.1.9 on 2024-05-15 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plazeduca', '0003_alter_alumnos_fecha_nac'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignaturas',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('horas_semanales', models.IntegerField()),
                ('num_alumnos', models.IntegerField()),
                ('profesor', models.CharField(max_length=9)),
                ('curso', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Asginaturas',
        ),
    ]