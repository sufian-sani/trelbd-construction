# Generated by Django 3.2 on 2022-05-30 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0029_auto_20220530_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='apply',
        ),
    ]
