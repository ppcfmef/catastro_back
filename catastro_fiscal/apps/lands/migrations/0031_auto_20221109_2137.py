# Generated by Django 3.2.15 on 2022-11-09 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0030_auto_20221014_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temploraluploadrecord',
            name='status',
            field=models.CharField(choices=[('INITIAL', 'Initiated'), ('IN_PROGRESS', 'In Progress'), ('LOADED', 'Loaded'), ('ERROR', 'Error Loaded')], max_length=20),
        ),
        migrations.AlterField(
            model_name='temploraluploadrecord',
            name='upload_status',
            field=models.CharField(choices=[('INITIAL', 'Initiated'), ('IN_PROGRESS', 'In Progress'), ('LOADED', 'Loaded'), ('ERROR', 'Error Loaded')], default='INITIAL', max_length=20),
        ),
        migrations.AlterField(
            model_name='uploadhistory',
            name='status',
            field=models.CharField(choices=[('INITIAL', 'Initiated'), ('IN_PROGRESS', 'In Progress'), ('LOADED', 'Loaded'), ('ERROR', 'Error Loaded')], default='INITIAL', max_length=20),
        ),
    ]
