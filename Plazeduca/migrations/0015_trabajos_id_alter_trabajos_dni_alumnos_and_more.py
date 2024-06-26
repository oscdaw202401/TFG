# Generated by Django 5.0.6 on 2024-06-02 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plazeduca', '0014_rename_faltas_asistencias_num_faltas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajos',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trabajos',
            name='dni_alumnos',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterUniqueTogether(
            name='trabajos',
            unique_together={('dni_alumnos', 'trabajo')},
        ),
    ]
