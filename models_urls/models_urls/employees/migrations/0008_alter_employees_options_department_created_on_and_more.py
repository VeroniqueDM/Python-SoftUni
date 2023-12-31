# Generated by Django 4.0.2 on 2022-02-26 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employees',
            options={'ordering': ('first_name', '-last_name')},
        ),
        migrations.AddField(
            model_name='department',
            name='created_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
