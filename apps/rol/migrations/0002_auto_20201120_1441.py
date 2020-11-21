# Generated by Django 3.0.3 on 2020-11-20 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='choices',
            field=models.CharField(choices=[('user_cre', 'user_creation'), ('user_list', 'user_list'), ('user_del', 'user_delete'), ('user_edit', 'user_edit'), ('rol_cre', 'rol_creation'), ('rol_list', 'rol_creation'), ('rol_edit', 'rol_edit'), ('rol_del', 'rol_delete'), ('proy_cre', 'project_creation'), ('proy_list', 'project_creation'), ('proy_edit', 'project_edit'), ('proy_del', 'project_delete'), ('task_cre', 'task_creation'), ('task_list', 'task_creation'), ('task_edit', 'task_edit'), ('task_del', 'tasl_delete'), ('lb_cre', 'lb_creation'), ('lb_list', 'lb_creation'), ('lb_edit', 'lb_edit'), ('lb_del', 'lb_delete')], max_length=100, null=True),
        ),
    ]
