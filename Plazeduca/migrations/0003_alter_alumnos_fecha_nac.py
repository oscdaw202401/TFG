# Generated by Django 4.1.9 on 2024-04-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plazeduca', '0002_notas_fecha_subida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='fecha_nac',
            field=models.DateTimeField(),
        ),
    ]
