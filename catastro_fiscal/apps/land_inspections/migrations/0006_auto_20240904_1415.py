# Generated by Django 3.2.19 on 2024-09-04 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0018_rename_masterpropertytype_mastertipopredio'),
        ('land_inspections', '0005_alter_location_cod_ubicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landcharacteristic',
            name='estado_conserva',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master_data.mastertipoestadoconservacion'),
        ),
        migrations.AlterField(
            model_name='landcharacteristic',
            name='material_pred',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master_data.mastertipomaterial'),
        ),
    ]
