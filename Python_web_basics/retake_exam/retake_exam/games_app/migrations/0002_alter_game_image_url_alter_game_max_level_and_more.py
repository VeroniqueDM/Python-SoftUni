# Generated by Django 4.0.4 on 2022-04-19 08:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='game',
            name='max_level',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Max Level'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.URLField(blank=True, null=True, verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Last Name'),
        ),
    ]
