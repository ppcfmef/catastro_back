# Generated by Django 3.2.19 on 2024-04-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0009_result_resolution_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='id_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Reasignar ubicación'), (2, 'Acumular'), (3, 'SubDividir'), (4, 'Inactivar'), (5, 'Independizar')], db_column='tipo', null=True),
        ),
    ]