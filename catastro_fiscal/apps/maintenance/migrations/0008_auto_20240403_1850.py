# Generated by Django 3.2.19 on 2024-04-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0007_alter_application_id_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='id_status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Por atender'), (2, 'Atendido'), (3, 'Observado'), (4, 'De baja')], db_column='estado', null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='id_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Reasignar ubicación'), (2, 'Acumular'), (3, 'Dividir'), (4, 'Inactivar'), (5, 'Independizar')], db_column='tipo', null=True),
        ),
    ]
