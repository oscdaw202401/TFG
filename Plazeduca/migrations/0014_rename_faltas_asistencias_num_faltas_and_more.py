# Generated by Django 5.0.6 on 2024-06-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plazeduca', '0013_rename_num_faltas_asistencias_faltas_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asistencias',
            old_name='faltas',
            new_name='num_faltas',
        ),
        migrations.RenameField(
            model_name='asistencias',
            old_name='retrasos',
            new_name='num_retrasos',
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='faltas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='retrasos',
            field=models.IntegerField(),
        ),
    ]
