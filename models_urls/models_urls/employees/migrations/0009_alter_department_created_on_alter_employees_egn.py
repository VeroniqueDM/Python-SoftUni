# Generated by Django 4.0.2 on 2022-02-27 04:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_alter_employees_options_department_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='egn',
            field=models.CharField(max_length=10, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='EGN'),
        ),
    ]