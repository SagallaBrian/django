# Generated by Django 4.1.1 on 2022-09-17 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mismain', '0003_rename_createad_department_created_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='createdby',
        ),
    ]