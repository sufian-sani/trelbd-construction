# Generated by Django 3.2 on 2022-05-29 07:01

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_remove_ourvision_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ourreport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('textfiled', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
    ]
