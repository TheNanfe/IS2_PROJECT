# Generated by Django 3.0.3 on 2020-11-20 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0002_auto_20201120_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='choices',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
