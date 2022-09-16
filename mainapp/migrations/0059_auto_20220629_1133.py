# Generated by Django 3.2 on 2022-06-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0058_alter_ourreport_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ourserver',
            options={'verbose_name': 'Our server', 'verbose_name_plural': 'Our server'},
        ),
        migrations.AddField(
            model_name='ourserver',
            name='brochure_file',
            field=models.FileField(blank=True, null=True, upload_to='brochure/'),
        ),
    ]
