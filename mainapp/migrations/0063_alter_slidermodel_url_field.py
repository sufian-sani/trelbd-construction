# Generated by Django 3.2 on 2022-07-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0062_slidermodel_url_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slidermodel',
            name='url_field',
            field=models.URLField(blank=True, default='#', null=True),
        ),
    ]