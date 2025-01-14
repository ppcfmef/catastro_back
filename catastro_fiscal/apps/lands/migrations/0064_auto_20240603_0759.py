# Generated by Django 3.2.19 on 2024-06-03 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0063_landowner_tipo_contribuyente'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='lote_urbano_puerta',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='land',
            name='manzana_urbana_puerta',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='landaudit',
            name='lote_urbano_puerta',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='landaudit',
            name='manzana_urbana_puerta',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
