# Generated by Django 3.2.19 on 2024-04-29 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0004_auto_20221127_0042'),
        ('land_inspections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='cod_tipo_uu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master_data.mastertypeurbanunit'),
        ),
    ]