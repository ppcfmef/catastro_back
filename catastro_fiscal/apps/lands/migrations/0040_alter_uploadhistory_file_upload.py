# Generated by Django 3.2.16 on 2023-05-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0039_auto_20230419_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadhistory',
            name='file_upload',
            field=models.FileField(null=True, upload_to='lands/registry'),
        ),
    ]
