# Generated by Django 3.0.3 on 2020-11-21 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linea_base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineabase',
            name='id_tarea',
        ),
        migrations.AddField(
            model_name='lineabase',
            name='tareas',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
