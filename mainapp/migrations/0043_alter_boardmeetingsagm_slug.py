# Generated by Django 3.2 on 2022-06-08 06:34

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0042_boardmeetingsagm_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmeetingsagm',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
