# Generated by Django 3.2.16 on 2022-11-26 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0034_uploadhistory_ubigeo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land',
            name='apartment_number',
            field=models.CharField(blank=True, db_column='numero_departamento', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='assigned_address',
            field=models.CharField(blank=True, db_column='dir_asig', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='block',
            field=models.CharField(blank=True, db_column='block', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='build_status_desc',
            field=models.CharField(blank=True, db_column='estado_construccion_desc', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='built_area',
            field=models.FloatField(blank=True, db_column='area_construida', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='classification_land_desc',
            field=models.CharField(blank=True, db_column='clasificacion_predio_desc', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='cod_cuc',
            field=models.CharField(blank=True, db_column='cod_cuc', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='cod_land',
            field=models.CharField(blank=True, db_column='cod_lote', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='cod_mzn',
            field=models.CharField(blank=True, db_column='cod_mzn', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='cod_sect',
            field=models.CharField(blank=True, db_column='cod_sect', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='cod_street',
            field=models.CharField(blank=True, db_column='cod_via', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='cod_uu',
            field=models.CharField(blank=True, db_column='cod_uu', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='condominium',
            field=models.FloatField(blank=True, db_column='condominio', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='cpm',
            field=models.CharField(blank=True, db_column='cod_pre', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='cup',
            field=models.CharField(blank=True, db_column='cod_cpu', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='deduction',
            field=models.FloatField(blank=True, db_column='deduccion', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='floor',
            field=models.CharField(blank=True, db_column='piso', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='front_length',
            field=models.FloatField(blank=True, db_column='longitud_frente', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='group_use_desc',
            field=models.CharField(blank=True, db_column='grupo_uso_desc', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='habilitacion_name',
            field=models.CharField(blank=True, db_column='nom_uu', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='id_aranc',
            field=models.IntegerField(blank=True, db_column='id_aranc', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='id_cartographic_img',
            field=models.CharField(blank=True, db_column='id_imagen_cartografica', help_text='id cartographic image', max_length=26, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='id_land_cartographic',
            field=models.CharField(blank=True, db_column='id_predio_cartografico', help_text='id land cartographic', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='id_object_img',
            field=models.IntegerField(blank=True, db_column='id_imagen_objeto', help_text='id object image', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='id_plot',
            field=models.CharField(blank=True, db_column='id_lote', help_text='id plot', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='inactive_reason',
            field=models.TextField(blank=True, db_column='razon_inactivo', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='indoor',
            field=models.CharField(blank=True, db_column='interior', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='km',
            field=models.CharField(blank=True, db_column='km', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='land_area',
            field=models.FloatField(blank=True, db_column='area_terreno', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='landmark',
            field=models.CharField(blank=True, db_column='referencia', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='latitude',
            field=models.FloatField(blank=True, db_column='coor_y', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='location_park',
            field=models.CharField(blank=True, db_column='ubicacion_parque', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='longitude',
            field=models.FloatField(blank=True, db_column='coor_x', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='municipal_address',
            field=models.CharField(blank=True, db_column='dir_mun', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='municipal_number',
            field=models.CharField(blank=True, db_column='num_mun', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='number_inhabitants',
            field=models.IntegerField(blank=True, db_column='cantidad_habitantes', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='owner',
            field=models.ForeignKey(blank=True, db_column='id_propietario', null=True, on_delete=django.db.models.deletion.SET_NULL, to='lands.landowner'),
        ),
        migrations.AlterField(
            model_name='land',
            name='property_type',
            field=models.CharField(blank=True, db_column='tipo_predio', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='reference_name',
            field=models.CharField(blank=True, db_column='nom_ref', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='resolution_document',
            field=models.CharField(blank=True, db_column='ndoc_res', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='resolution_type',
            field=models.CharField(blank=True, db_column='tdoc_res', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='sec_ejec',
            field=models.CharField(blank=True, db_column='sec_ejec', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='self_assessment_affection',
            field=models.FloatField(blank=True, db_column='autoavaluo_afecto', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='self_assessment_total',
            field=models.FloatField(blank=True, db_column='autoavaluo_total', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='site',
            field=models.IntegerField(blank=True, db_column='lugar', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='source',
            field=models.CharField(blank=True, choices=[('carga_masiva', 'Carga Masiva'), ('asignar_lote', 'Asignar Lote'), ('asignar_img', 'Asignar Imagen')], db_column='origen', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='source_information',
            field=models.CharField(blank=True, db_column='fuente', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Sin Cartografia'), (1, 'Con cartografia (Lote)'), (2, 'Con cartografia (Imagen)'), (3, 'Inactivo')], db_column='estado', default=0, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='status_img',
            field=models.PositiveSmallIntegerField(blank=True, db_column='estado_imagen', null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='street_name',
            field=models.CharField(blank=True, db_column='nom_via', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='street_name_alt',
            field=models.CharField(blank=True, db_column='nom_alt', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='street_type',
            field=models.CharField(blank=True, db_column='tip_via', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='ubigeo',
            field=models.CharField(blank=True, db_column='ubigeo', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='urban_address',
            field=models.CharField(blank=True, db_column='dir_urb', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='urban_lot_number',
            field=models.CharField(blank=True, db_column='lot_urb', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='urban_mza',
            field=models.CharField(blank=True, db_column='mzn_urb', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='uu_type',
            field=models.CharField(blank=True, db_column='tipo_uu', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='apartment_number',
            field=models.CharField(blank=True, db_column='numero_departamento', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='assigned_address',
            field=models.CharField(blank=True, db_column='dir_asig', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='block',
            field=models.CharField(blank=True, db_column='block', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='build_status_desc',
            field=models.CharField(blank=True, db_column='estado_construccion_desc', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='built_area',
            field=models.FloatField(blank=True, db_column='area_construida', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='classification_land_desc',
            field=models.CharField(blank=True, db_column='clasificacion_predio_desc', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='cod_cuc',
            field=models.CharField(blank=True, db_column='cod_cuc', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='cod_land',
            field=models.CharField(blank=True, db_column='cod_lote', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='cod_mzn',
            field=models.CharField(blank=True, db_column='cod_mzn', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='cod_sect',
            field=models.CharField(blank=True, db_column='cod_sect', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='cod_street',
            field=models.CharField(blank=True, db_column='cod_via', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='cod_uu',
            field=models.CharField(blank=True, db_column='cod_uu', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='condominium',
            field=models.FloatField(blank=True, db_column='condominio', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='cpm',
            field=models.CharField(blank=True, db_column='cod_pre', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='cup',
            field=models.CharField(blank=True, db_column='cod_cpu', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='deduction',
            field=models.FloatField(blank=True, db_column='deduccion', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='floor',
            field=models.CharField(blank=True, db_column='piso', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='front_length',
            field=models.FloatField(blank=True, db_column='longitud_frente', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='group_use_desc',
            field=models.CharField(blank=True, db_column='grupo_uso_desc', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='habilitacion_name',
            field=models.CharField(blank=True, db_column='nom_uu', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='id_aranc',
            field=models.IntegerField(blank=True, db_column='id_aranc', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='id_cartographic_img',
            field=models.CharField(blank=True, db_column='id_imagen_cartografica', help_text='id cartographic image', max_length=26, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='id_land_cartographic',
            field=models.CharField(blank=True, db_column='id_predio_cartografico', help_text='id land cartographic', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='id_object_img',
            field=models.IntegerField(blank=True, db_column='id_imagen_objeto', help_text='id object image', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='id_plot',
            field=models.CharField(blank=True, db_column='id_lote', help_text='id plot', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='inactive_reason',
            field=models.TextField(blank=True, db_column='razon_inactivo', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='indoor',
            field=models.CharField(blank=True, db_column='interior', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='km',
            field=models.CharField(blank=True, db_column='km', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='land_area',
            field=models.FloatField(blank=True, db_column='area_terreno', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='landmark',
            field=models.CharField(blank=True, db_column='referencia', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='latitude',
            field=models.FloatField(blank=True, db_column='coor_y', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='location_park',
            field=models.CharField(blank=True, db_column='ubicacion_parque', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='longitude',
            field=models.FloatField(blank=True, db_column='coor_x', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='municipal_address',
            field=models.CharField(blank=True, db_column='dir_mun', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='municipal_number',
            field=models.CharField(blank=True, db_column='num_mun', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='number_inhabitants',
            field=models.IntegerField(blank=True, db_column='cantidad_habitantes', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='owner',
            field=models.ForeignKey(blank=True, db_column='id_propietario', null=True, on_delete=django.db.models.deletion.SET_NULL, to='lands.landowner'),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='property_type',
            field=models.CharField(blank=True, db_column='tipo_predio', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='reference_name',
            field=models.CharField(blank=True, db_column='nom_ref', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='resolution_document',
            field=models.CharField(blank=True, db_column='ndoc_res', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='resolution_type',
            field=models.CharField(blank=True, db_column='tdoc_res', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='sec_ejec',
            field=models.CharField(blank=True, db_column='sec_ejec', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='self_assessment_affection',
            field=models.FloatField(blank=True, db_column='autoavaluo_afecto', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='self_assessment_total',
            field=models.FloatField(blank=True, db_column='autoavaluo_total', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='site',
            field=models.IntegerField(blank=True, db_column='lugar', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='source',
            field=models.CharField(blank=True, choices=[('carga_masiva', 'Carga Masiva'), ('asignar_lote', 'Asignar Lote'), ('asignar_img', 'Asignar Imagen')], db_column='origen', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='source_information',
            field=models.CharField(blank=True, db_column='fuente', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Sin Cartografia'), (1, 'Con cartografia (Lote)'), (2, 'Con cartografia (Imagen)'), (3, 'Inactivo')], db_column='estado', default=0, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='status_img',
            field=models.PositiveSmallIntegerField(blank=True, db_column='estado_imagen', null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='street_name',
            field=models.CharField(blank=True, db_column='nom_via', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='street_name_alt',
            field=models.CharField(blank=True, db_column='nom_alt', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='street_type',
            field=models.CharField(blank=True, db_column='tip_via', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='ubigeo',
            field=models.CharField(blank=True, db_column='ubigeo', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='urban_address',
            field=models.CharField(blank=True, db_column='dir_urb', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='urban_lot_number',
            field=models.CharField(blank=True, db_column='lot_urb', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='urban_mza',
            field=models.CharField(blank=True, db_column='mzn_urb', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='landaudit',
            name='uu_type',
            field=models.CharField(blank=True, db_column='tipo_uu', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='landowner',
            name='code',
            field=models.CharField(blank=True, db_column='cod_contr', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='landowner',
            name='description_owner',
            field=models.CharField(blank=True, db_column='contribuyente', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='landowner',
            name='dni',
            field=models.CharField(db_column='doc_iden', max_length=20),
        ),
        migrations.AlterField(
            model_name='landowner',
            name='document_type',
            field=models.CharField(blank=True, db_column='tip_doc', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='landowner',
            name='email',
            field=models.CharField(blank=True, db_column='correo_electronico', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='landowner',
            name='maternal_surname',
            field=models.CharField(blank=True, db_column='ap_mat', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='landowner',
            name='name',
            field=models.CharField(blank=True, db_column='nombre', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='landowner',
            name='number_lands',
            field=models.IntegerField(blank=True, db_column='numero_tierras', default=0, null=True),
        ),
        migrations.AlterField(
            model_name='landowner',
            name='paternal_surname',
            field=models.CharField(blank=True, db_column='ap_pat', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='landowner',
            name='phone',
            field=models.CharField(blank=True, db_column='telefono', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='landowner',
            name='tax_address',
            field=models.CharField(blank=True, db_column='dir_fiscal', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landowner',
            name='upload_history',
            field=models.ForeignKey(blank=True, db_column='historial_carga', null=True, on_delete=django.db.models.deletion.SET_NULL, to='lands.uploadhistory'),
        ),
    ]
