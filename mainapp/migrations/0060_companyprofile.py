# Generated by Django 3.2 on 2022-06-29 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0059_auto_20220629_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companyprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='companyprofile/')),
            ],
            options={
                'verbose_name': 'Company Profile',
                'verbose_name_plural': 'Company Profile',
            },
        ),
    ]
