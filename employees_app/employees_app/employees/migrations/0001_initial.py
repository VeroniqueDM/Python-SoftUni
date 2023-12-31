# Generated by Django 4.0.3 on 2022-04-01 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=40, null=True)),
                ('egn', models.CharField(max_length=10, unique=True, verbose_name='EGN')),
                ('job_title_t', models.IntegerField(choices=[(1, 'Python Dev'), (2, 'QA Engineer'), (3, 'DevOps Specialist')])),
                ('company', models.CharField(choices=[('SoftUni', 'SoftUni'), ('Google', 'Google'), ('Facebook', 'Facebook')], max_length=8)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.department')),
            ],
        ),
    ]
