# Generated by Django 3.2.19 on 2024-08-27 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0015_materestadoconserva_matermaterial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MaterEstadoConserva',
            new_name='MasterEstadoConserva',
        ),
        migrations.RenameModel(
            old_name='MaterMaterial',
            new_name='MasterMaterial',
        ),
    ]
