# Generated by Django 3.2 on 2022-05-30 08:00

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_reportstatement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsevents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='photos/Newsevents')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='reportstatement',
            options={'verbose_name': 'Report and Statement', 'verbose_name_plural': 'Report and Statement'},
        ),
    ]