# Generated by Django 2.2.3 on 2020-08-21 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0002_auto_20200821_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='observacion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
