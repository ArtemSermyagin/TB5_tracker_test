# Generated by Django 5.0.6 on 2024-06-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='position',
            new_name='job_title',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='deadline',
            new_name='completion_date',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='executor',
            new_name='employer_id',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='status',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='parent_task',
            new_name='parent',
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(default='default_value', max_length=100),
        ),
    ]