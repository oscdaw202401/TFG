# Generated by Django 4.1.9 on 2024-03-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('usuario', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('email', models.EmailField(max_length=50)),
                ('dirreccion', models.CharField(max_length=50)),
                ('cursos', models.CharField(max_length=20)),
                ('faltas', models.IntegerField()),
                ('retrasos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Asginaturas',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('horas_semanales', models.IntegerField()),
                ('dni_alumnos', models.CharField(max_length=9)),
                ('dni_profesor', models.CharField(max_length=9)),
                ('curso', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Asistencias',
            fields=[
                ('dni_alumnos', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('num_faltas', models.IntegerField()),
                ('num_retrasos', models.IntegerField()),
                ('nom_asignatura', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('dni_profesor', models.CharField(max_length=50)),
                ('dni_alumnos', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('fecha_envio', models.DateField()),
                ('motivo', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('siglas', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('nota', models.IntegerField()),
                ('dni_alumno', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nom_asignatura', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('usuario', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('email', models.EmailField(max_length=50)),
                ('dirreccion', models.CharField(max_length=50)),
                ('cursos', models.CharField(max_length=20)),
                ('tutoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajos',
            fields=[
                ('trabajo', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_entrega', models.DateField()),
                ('dni_alumnos', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nom_asignatura', models.CharField(max_length=50)),
            ],
        ),
    ]
