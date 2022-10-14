# Generated by Django 3.2.15 on 2022-10-14 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0025_alter_landowner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Sin Cartografia'), (1, 'Con cartografia (Lote)'), (2, 'Con cartografia (Imagen)'), (3, 'Inactivo')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Sin Cartografia'), (1, 'Con cartografia (Lote)'), (2, 'Con cartografia (Imagen)'), (3, 'Inactivo')], default=0, null=True),
        ),
    ]
