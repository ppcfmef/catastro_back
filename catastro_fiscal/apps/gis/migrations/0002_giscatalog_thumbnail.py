# Generated by Django 3.2.15 on 2022-11-09 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='giscatalog',
            name='thumbnail',
            field=models.FileField(blank=True, default=None, null=True, upload_to='gis'),
        ),
    ]
