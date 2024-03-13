# Generated by Django 3.2.19 on 2024-02-26 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lands', '0054_auto_20240226_0929'),
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
            name='LandInspection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ubigeo', models.CharField(max_length=6)),
                ('cod_cpu', models.CharField(blank=True, max_length=50, null=True)),
                ('cod_pre', models.CharField(blank=True, max_length=50, null=True)),
                ('piso', models.CharField(blank=True, max_length=100, null=True)),
                ('num_sumi_agua', models.CharField(blank=True, max_length=100, null=True)),
                ('num_sumi_luz', models.CharField(blank=True, max_length=100, null=True)),
                ('uso_especifico', models.CharField(blank=True, max_length=100, null=True)),
                ('interior', models.CharField(blank=True, max_length=100, null=True)),
                ('obs_predio', models.CharField(blank=True, max_length=100, null=True)),
                ('num_dpto', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo_uso', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
                ('block', models.CharField(blank=True, max_length=100, null=True)),
                ('num_sumi_gas', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Land Inspection',
                'verbose_name_plural': 'Lands Inspection',
                'db_table': 'TB_PREDIO_INSPEC',
            },
        ),
        migrations.CreateModel(
            name='LandInspectionType',
            fields=[
                ('cod_tipo_predio', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('desc_tipo_predio', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Facility Type',
                'verbose_name_plural': 'Land Inspection Types',
                'db_table': 'TB_TIP_PREDIO_INSPEC',
            },
        ),
        migrations.CreateModel(
            name='LandInspectionUpload',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cod_carga', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=150)),
                ('user', models.ForeignKey(blank=True, db_column='cod_usuario', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Land Inspection',
                'verbose_name_plural': 'Lands Inspection Upload',
                'db_table': 'TB_INSPECCION_PREDIAL',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('cod_ubicacion', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cod_tip_via', models.CharField(blank=True, max_length=10, null=True)),
                ('cod_via', models.CharField(blank=True, max_length=255, null=True)),
                ('nom_via', models.CharField(blank=True, max_length=255, null=True)),
                ('num_alt', models.CharField(blank=True, max_length=255, null=True)),
                ('nom_alt', models.CharField(blank=True, max_length=255, null=True)),
                ('cod_tipo_uu', models.CharField(blank=True, max_length=255, null=True)),
                ('cod_uu', models.CharField(blank=True, max_length=255, null=True)),
                ('nom_uu', models.CharField(blank=True, max_length=255, null=True)),
                ('nom_ref', models.CharField(blank=True, max_length=255, null=True)),
                ('km', models.CharField(blank=True, max_length=255, null=True)),
                ('x', models.FloatField(blank=True, db_column='coor_x', null=True)),
                ('y', models.FloatField(blank=True, db_column='coor_y', null=True)),
                ('lot_urb', models.CharField(blank=True, max_length=255, null=True)),
                ('num_mun', models.CharField(blank=True, max_length=255, null=True)),
                ('mzn_urb', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('cod_usuario', models.CharField(blank=True, max_length=255, null=True)),
                ('obs_ubicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('referencia', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'pendiente'), (6, 'resuelto'), (98, 'observado')], db_column='estado', default=0, null=True)),
                ('file_obs', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Location',
                'db_table': 'TB_UBICACION',
            },
        ),
        migrations.CreateModel(
            name='OwnerShipType',
            fields=[
                ('cod_tipo_tit', models.AutoField(primary_key=True, serialize=False)),
                ('desc_tipo_tit', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'OwnerShip Type',
                'verbose_name_plural': 'OwnerShip Type',
                'db_table': 'TB_TIPO_TITULARIDAD',
            },
        ),
        migrations.CreateModel(
            name='PhotoType',
            fields=[
                ('cod_tipo_foto', models.AutoField(primary_key=True, serialize=False)),
                ('desc_tipo_foto', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Photo Type',
                'verbose_name_plural': 'Photo Type',
                'db_table': 'TB_TIPO_FOTO',
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
                'verbose_name_plural': 'Supply Types',
                'db_table': 'TB_TIPO_SUMINISTRO',
            },
        ),
        migrations.CreateModel(
            name='TicketSendStation',
            fields=[
                ('cod_est_envio_ticket', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('desc_est_envio_ticket', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Ticket Send state',
                'verbose_name_plural': 'Ticket Send state',
                'db_table': 'TB_EST_ENVIO_TICKET',
            },
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('cod_tipo_ticket', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('desc_tipo_ticket', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Ticket Type',
                'verbose_name_plural': 'Ticket Types',
                'db_table': 'TB_TIPO_TICKET',
            },
        ),
        migrations.CreateModel(
            name='TicketWorkStation',
            fields=[
                ('cod_est_trabajo_ticket', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('desc_est_trabajo_ticket', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Ticket Work state',
                'verbose_name_plural': 'Ticket Work state',
                'db_table': 'TB_EST_TRABAJO_TICKET',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('cod_ticket', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('cod_usuario', models.CharField(blank=True, max_length=255, null=True)),
                ('obs_ticket_usuario', models.CharField(blank=True, max_length=255, null=True)),
                ('fec_inicio_trabajo', models.DateTimeField(blank=True, null=True)),
                ('fec_asignacion', models.DateTimeField(blank=True, null=True)),
                ('fec_ultima_actualizacion', models.DateTimeField(blank=True, null=True)),
                ('obs_ticket_gabinete', models.CharField(blank=True, max_length=255, null=True)),
                ('nro_notificacion', models.IntegerField(blank=True, default=0, null=True)),
                ('cod_est_envio_ticket', models.ForeignKey(blank=True, db_column='cod_est_envio_ticket', null=True, on_delete=django.db.models.deletion.SET_NULL, to='land_inspections.ticketsendstation')),
                ('cod_est_trabajo_ticket', models.ForeignKey(blank=True, db_column='cod_est_trabajo_ticket', null=True, on_delete=django.db.models.deletion.SET_NULL, to='land_inspections.ticketworkstation')),
                ('cod_tipo_ticket', models.ForeignKey(blank=True, db_column='cod_tipo_ticket', null=True, on_delete=django.db.models.deletion.SET_NULL, to='land_inspections.tickettype')),
                ('inspection_upload', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='land_inspections.landinspectionupload')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Ticket',
                'db_table': 'TB_TICKET',
            },
        ),
        migrations.CreateModel(
            name='RecordOwnerShip',
            fields=[
                ('cod_tit', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ubigeo', models.CharField(blank=True, default=None, max_length=6, null=True)),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'pendiente'), (6, 'resuelto'), (98, 'observado')], db_column='estado', default=0, null=True)),
                ('file_notificacion', models.FileField(blank=True, null=True, upload_to='')),
                ('cod_tipo_tit', models.ForeignKey(blank=True, db_column='cod_tipo_tit', null=True, on_delete=django.db.models.deletion.SET_NULL, to='land_inspections.ownershiptype')),
                ('cod_ubicacion', models.ForeignKey(db_column='cod_ubicacion', on_delete=django.db.models.deletion.CASCADE, related_name='registros_titularidad', to='land_inspections.location')),
            ],
            options={
                'verbose_name': 'OwnerShip',
                'verbose_name_plural': 'OwnerShip',
                'db_table': 'TB_REGISTRO_TITULARIDAD',
            },
        ),
        migrations.CreateModel(
            name='LocationPhoto',
            fields=[
                ('cod_foto', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='land_inspections')),
                ('cod_tipo_foto', models.ForeignKey(db_column='cod_tipo_foto', on_delete=django.db.models.deletion.CASCADE, to='land_inspections.phototype')),
                ('cod_ubicacion', models.ForeignKey(db_column='cod_ubicacion', on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='land_inspections.location')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photo',
                'db_table': 'TB_FOTOS',
            },
        ),
        migrations.AddField(
            model_name='location',
            name='cod_ticket',
            field=models.ForeignKey(db_column='cod_ticket', on_delete=django.db.models.deletion.CASCADE, related_name='ubicaciones', to='land_inspections.ticket'),
        ),
        migrations.CreateModel(
            name='LandSupply',
            fields=[
                ('cod_suministro', models.AutoField(primary_key=True, serialize=False)),
                ('num_sumis', models.CharField(blank=True, max_length=20, null=True)),
                ('obs_sumis', models.CharField(blank=True, max_length=100, null=True)),
                ('cod_contr', models.ForeignKey(blank=True, db_column='cod_contr', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='suministro', to='lands.landowner')),
                ('cod_tipo_sumi', models.ForeignKey(blank=True, db_column='cod_tipo_sumi', null=True, on_delete=django.db.models.deletion.SET_NULL, to='land_inspections.supplytype')),
                ('cod_tit', models.OneToOneField(db_column='cod_tit', on_delete=django.db.models.deletion.CASCADE, related_name='suministro', to='land_inspections.recordownership')),
            ],
            options={
                'verbose_name': 'Land Supply',
                'verbose_name_plural': 'Land Supplies',
                'db_table': 'TB_SUMINISTRO',
            },
        ),
        migrations.CreateModel(
            name='LandOwnerInspection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cod_contr', models.CharField(blank=True, max_length=50, null=True)),
                ('tip_doc', models.CharField(blank=True, max_length=2, null=True)),
                ('doc_iden', models.CharField(blank=True, max_length=20, null=True)),
                ('dir_fiscal', models.CharField(blank=True, max_length=255, null=True)),
                ('ap_mat', models.CharField(blank=True, max_length=100, null=True)),
                ('ap_pat', models.CharField(blank=True, max_length=150, null=True)),
                ('cond_contr', models.CharField(blank=True, max_length=150, null=True)),
                ('contribuyente', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('conyuge', models.CharField(blank=True, max_length=100, null=True)),
                ('cod_tit', models.ForeignKey(db_column='cod_tit', on_delete=django.db.models.deletion.CASCADE, to='land_inspections.recordownership')),
            ],
            options={
                'verbose_name': 'Land Owner Inspection',
                'verbose_name_plural': 'Land Owner Inspection',
                'db_table': 'TB_CONTRIBUYENTE_INSPEC',
            },
        ),
        migrations.CreateModel(
            name='LandOwnerDetailInspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubigeo', models.CharField(max_length=6)),
                ('doc_iden', models.CharField(blank=True, max_length=20, null=True)),
                ('cod_pre', models.CharField(blank=True, max_length=50, null=True)),
                ('cod_contr_inspec', models.ForeignKey(db_column='cod_contr_inspec', on_delete=django.db.models.deletion.CASCADE, related_name='contribuyentes', to='land_inspections.landownerinspection')),
                ('cod_pred_inspec', models.ForeignKey(db_column='cod_pred_inspec', on_delete=django.db.models.deletion.CASCADE, related_name='predio_contribuyente', to='land_inspections.landinspection')),
                ('cod_tit', models.ForeignKey(db_column='cod_tit', on_delete=django.db.models.deletion.CASCADE, to='land_inspections.recordownership')),
            ],
            options={
                'verbose_name': 'Land Inspection',
                'verbose_name_plural': 'Lands Owner Detail Inspection',
                'db_table': 'TB_PREDIO_CONTRIBUYENTE_INSPEC',
            },
        ),
        migrations.AddField(
            model_name='landinspection',
            name='cod_tipo_predio',
            field=models.ForeignKey(blank=True, db_column='cod_tipo_predio', null=True, on_delete=django.db.models.deletion.SET_NULL, to='land_inspections.landinspectiontype'),
        ),
        migrations.AddField(
            model_name='landinspection',
            name='cod_tit',
            field=models.OneToOneField(db_column='cod_tit', on_delete=django.db.models.deletion.CASCADE, related_name='predio_inspeccion', to='land_inspections.recordownership'),
        ),
        migrations.CreateModel(
            name='LandFacility',
            fields=[
                ('cod_inst', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('anio_construccion', models.CharField(blank=True, max_length=20, null=True)),
                ('estado_conserva', models.CharField(blank=True, max_length=255, null=True)),
                ('dimension', models.CharField(blank=True, max_length=100, null=True)),
                ('cod_tipo_inst', models.ForeignKey(blank=True, db_column='cod_tipo_inst', null=True, on_delete=django.db.models.deletion.SET_NULL, to='land_inspections.facilitytype')),
                ('cod_tit', models.ForeignKey(db_column='cod_tit', on_delete=django.db.models.deletion.CASCADE, related_name='instalaciones', to='land_inspections.recordownership')),
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
                ('cod_tit', models.OneToOneField(db_column='cod_tit', on_delete=django.db.models.deletion.CASCADE, related_name='caracteristicas', to='land_inspections.recordownership')),
            ],
            options={
                'verbose_name': 'Land Characteristic',
                'verbose_name_plural': 'Land Characteristics',
                'db_table': 'TB_CARACTERISTICAS',
            },
        ),
    ]
