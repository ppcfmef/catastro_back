# Generated by Django 3.2.19 on 2024-08-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land_inspections', '0003_auto_20240801_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landfacility',
            name='cod_inst',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='landsupply',
            name='num_sumis',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='recordownership',
            name='cod_tit',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]