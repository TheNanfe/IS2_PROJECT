# Generated by Django 3.0.3 on 2020-11-21 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linea_base', '0002_auto_20201120_2133'),
        ('tarea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='id_lineabase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='linea_base.LineaBase'),
        ),
    ]
