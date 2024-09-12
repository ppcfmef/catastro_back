# Generated by Django 3.2.19 on 2024-09-12 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_district_sec_ejec'),
        ('land_inspections', '0012_auto_20240912_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordownership',
            name='ubigeo',
            field=models.ForeignKey(blank=True, db_column='ubigeo', null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.district'),
        ),
    ]
