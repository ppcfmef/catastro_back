# Generated by Django 3.2.23 on 2024-01-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land_inspections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordownership',
            name='file_notificacion',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='ticket',
            name='nro_notificacion',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
