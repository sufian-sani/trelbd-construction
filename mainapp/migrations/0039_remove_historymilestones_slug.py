# Generated by Django 3.2 on 2022-06-08 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0038_historymilestones_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historymilestones',
            name='slug',
        ),
    ]
