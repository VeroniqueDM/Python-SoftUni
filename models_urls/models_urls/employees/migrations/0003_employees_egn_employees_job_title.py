# Generated by Django 4.0.2 on 2022-02-26 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employees_first_name_employees_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='egn',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='job_title',
            field=models.IntegerField(choices=[(1, 'Software Engineer'), (2, 'Dev Ops'), (3, 'QA')], null=True),
        ),
    ]
