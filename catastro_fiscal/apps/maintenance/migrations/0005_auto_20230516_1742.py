# Generated by Django 3.2.18 on 2023-05-16 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0004_alter_applicationobservationdetail_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='support',
            field=models.FileField(blank=True, db_column='sustento', null=True, upload_to='sustento/'),
        ),
        migrations.AlterField(
            model_name='application',
            name='id_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Reasignar ubicación'), (2, 'Acumulación'), (3, 'División'), (4, 'Inactivar')], db_column='tipo', null=True),
        ),
    ]
