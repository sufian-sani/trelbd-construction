# Generated by Django 3.2 on 2022-05-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0028_auto_20220530_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='job_id',
            field=models.CharField(default='1', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='job_title',
            field=models.CharField(default='manager', max_length=300),
            preserve_default=False,
        ),
    ]
