# Generated by Django 3.2.19 on 2024-03-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0054_auto_20240226_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='municipal_number_alt',
            field=models.CharField(blank=True, db_column='num_alt', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='landaudit',
            name='municipal_number_alt',
            field=models.CharField(blank=True, db_column='num_alt', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='municipal_number',
            field=models.CharField(blank=True, db_column='num_mun', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='municipal_number',
            field=models.CharField(blank=True, db_column='num_mun', max_length=10, null=True),
        ),
    ]
