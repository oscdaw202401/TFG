# Generated by Django 5.0.6 on 2024-05-31 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Plazeduca', '0006_citas_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citas',
            name='id',
        ),
    ]