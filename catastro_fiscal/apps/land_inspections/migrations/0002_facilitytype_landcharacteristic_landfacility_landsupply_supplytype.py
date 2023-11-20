# Generated by Django 3.2.19 on 2023-10-29 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('land_inspections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilityType',
            fields=[
                ('cod_tipo_inst', models.AutoField(primary_key=True, serialize=False)),
                ('desc_tipo_inst', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Facility type',
                'verbose_name_plural': 'Facility types',
                'db_table': 'TB_TIPO_INSTA',
            },
        ),
        migrations.CreateModel(
            name='SupplyType',
            fields=[
                ('cod_tipo_sumi', models.AutoField(primary_key=True, serialize=False)),
                ('desc_tipo_sumi', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Facility Type',
                'verbose_name_plural': 'Facility Types',
                'db_table': 'TB_TIPO_SUMINISTRO',
            },
        ),
        migrations.CreateModel(
            name='LandSupply',
            fields=[
                ('cod_suministro', models.AutoField(primary_key=True, serialize=False)),
                ('num_sumis', models.CharField(blank=True, max_length=20, null=True)),
                ('obs_sumis', models.CharField(blank=True, max_length=100, null=True)),
                ('cod_tipo_sumi', models.ForeignKey(blank=True, db_column='cod_tipo_sumi', null=True, on_delete=django.db.models.deletion.SET_NULL, to='land_inspections.supplytype')),
                ('cod_tit', models.ForeignKey(db_column='cod_tit', on_delete=django.db.models.deletion.CASCADE, to='land_inspections.recordownership')),
            ],
            options={
                'verbose_name': 'Land Supply',
                'verbose_name_plural': 'Land Supplies',
                'db_table': 'TB_SUMINISTRO',
            },
        ),
        migrations.CreateModel(
            name='LandFacility',
            fields=[
                ('cod_inst', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('anio_construccion', models.CharField(blank=True, max_length=20, null=True)),
                ('estado_conserva', models.CharField(blank=True, max_length=255, null=True)),
                ('dimension', models.CharField(blank=True, max_length=100, null=True)),
                ('cod_tipo_inst', models.ForeignKey(blank=True, db_column='cod_tipo_inst', null=True, on_delete=django.db.models.deletion.SET_NULL, to='land_inspections.facilitytype')),
                ('cod_tit', models.ForeignKey(db_column='cod_tit', on_delete=django.db.models.deletion.CASCADE, to='land_inspections.recordownership')),
            ],
            options={
                'verbose_name': 'Land Facility',
                'verbose_name_plural': 'Land Facilities',
                'db_table': 'TB_INSTALACIONES',
            },
        ),
        migrations.CreateModel(
            name='LandCharacteristic',
            fields=[
                ('cod_caracteristica', models.AutoField(primary_key=True, serialize=False)),
                ('categoria_electrica', models.CharField(blank=True, max_length=100, null=True)),
                ('piso', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_conserva', models.CharField(blank=True, max_length=100, null=True)),
                ('anio_construccion', models.CharField(blank=True, max_length=100, null=True)),
                ('catergoria_techo', models.CharField(blank=True, max_length=100, null=True)),
                ('longitud_frente', models.FloatField(blank=True, null=True)),
                ('categoria_muro_columna', models.CharField(blank=True, max_length=100, null=True)),
                ('catergoria_puerta_ventana', models.CharField(blank=True, max_length=100, null=True)),
                ('arancel', models.FloatField(blank=True, null=True)),
                ('material_pred', models.CharField(blank=True, max_length=100, null=True)),
                ('categoria_revestimiento', models.CharField(blank=True, max_length=100, null=True)),
                ('area_terreno', models.FloatField(blank=True, null=True)),
                ('clasificacion_pred', models.CharField(blank=True, max_length=100, null=True)),
                ('catergoria_piso', models.CharField(blank=True, max_length=100, null=True)),
                ('catergoria_bano', models.CharField(blank=True, max_length=100, null=True)),
                ('area_construida', models.FloatField(blank=True, null=True)),
                ('cod_tit', models.ForeignKey(db_column='cod_tit', on_delete=django.db.models.deletion.CASCADE, to='land_inspections.recordownership')),
            ],
            options={
                'verbose_name': 'Land Characteristic',
                'verbose_name_plural': 'Land Characteristics',
                'db_table': 'TB_CARACTERISTICAS',
            },
        ),
    ]