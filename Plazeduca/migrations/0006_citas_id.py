# Generated by Django 5.0.6 on 2024-05-31 15:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plazeduca', '0005_rename_dirreccion_alumnos_direccion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='citas',
            name='id',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
