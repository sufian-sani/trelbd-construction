# Generated by Django 3.2 on 2022-06-12 06:11

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0049_noticesection'),
    ]

    operations = [
        migrations.AddField(
            model_name='corporategovernance',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='ghdgjfgdjkfgj', editable=False, populate_from='title'),
            preserve_default=False,
        ),
    ]
