# Generated by Django 3.2.19 on 2024-09-12 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0019_mastertipoobracomplementaria'),
        ('land_inspections', '0008_auto_20240905_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landfacility',
            name='cod_tipo_inst',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cod_tipo_inst', to='master_data.mastertipoobracomplementaria'),
        ),
        migrations.AlterField(
            model_name='landfacility',
            name='estado_conserva',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master_data.mastertipoestadoconservacion'),
        ),
    ]
