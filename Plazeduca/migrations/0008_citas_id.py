# Generated by Django 5.0.6 on 2024-05-31 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plazeduca', '0007_remove_citas_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='citas',
            name='id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
