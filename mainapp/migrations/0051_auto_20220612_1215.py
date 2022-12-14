# Generated by Django 3.2 on 2022-06-12 06:15

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0050_corporategovernance_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='corporategovernance',
            options={'verbose_name': 'Corporate Governance', 'verbose_name_plural': 'Corporate Governance'},
        ),
        migrations.AlterField(
            model_name='corporategovernance',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
