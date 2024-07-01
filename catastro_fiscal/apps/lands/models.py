from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import AbstractAudit
from apps.places.models import District
from apps.master_data.models import MasterCodeStreet , MasterTipoPropiedad, MasterTipoTransferencia,MasterTipoUsoPredio,MasterTipoDocumentoIdentidad, MasterTipoContribuyente, MasterTipoNivel,MasterTipoEstadoConservacion,MasterTipoMaterial


class UploadHistory(models.Model):
    STATUS_CHOICE = (
        ('INITIAL', _('Initiated')),
        ('IN_PROGRESS_TMP', _('In Progress Temporal')),
        ('LOADED_TMP', _('Loaded Temporal')),
        ('IN_PROGRESS', _('In Progress')),
        ('LOADED', _('Loaded')),
        ('ERROR', _('Error Loaded')),
        ('CANCEL', _('Cancel by user')),
        ('LOADED_START', _('Carga Inicial')),
    )

    TYPE_UPLOAD_CHOICE = (
        ('TB_PREDIO', _('TB_PREDIO')),
        ('RT_CONTRIBUYENTE', _('RT_CONTRIBUYENTE')),
        ('RT_MARCO_PREDIO', _('RT_MARCOPREDIO')),
        ('RT_ARANCEL', _('RT_ARANCEL')),
        ('RT_PREDIO_DATO', _('RT_PREDIO_DATO')),
        ('RT_PREDIO_CARACT', _('RT_PREDIO_CARACT')),
        ('RT_RECAUDACION', _('RT_RECAUDACION')),
        ('RT_DEUDA', _('RT_DEUDA')),
        ('RT_EMISION', _('RT_EMISION')),
        ('RT_BIMPONIBLE', _('RT_BIMPONIBLE')),
        ('RT_ALICUOTA', _('RT_ALICUOTA')),
        ('RT_AMNCONTRIBUYENTE', _('RT_AMNCONTRIBUYENTE')),
        ('RT_AMNMUNICIPAL', _('RT_AMNMUNICIPAL')),
        ('RT_VAREM_MUNI', _('RT_VAREM_MUNI')),
    )
    id = models.AutoField(primary_key=True)
    file_upload = models.FileField(upload_to='lands/registry', null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, default=None)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='INITIAL')
    type_upload = models.CharField(max_length=50, choices=TYPE_UPLOAD_CHOICE, default='TB_PREDIO')
    username = models.CharField(max_length=150)
    total_records = models.PositiveSmallIntegerField(null=True, default=None)
    total_new_records = models.PositiveSmallIntegerField(null=True, default=None)
    total_error_records = models.PositiveSmallIntegerField(null=True, default=None)
    total_update_records = models.PositiveSmallIntegerField(null=True, default=None)
    total_land = models.PositiveSmallIntegerField(null=True, default=None)
    total_land_mapping = models.PositiveSmallIntegerField(null=True, default=None)
    ubigeo = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'HISTORIAL_CARGA'
        verbose_name = _('upload history')
        verbose_name_plural = _('upload history')

    def __str__(self):
        return f'{self.id}'

    @property
    def total_land_notmapping(self):
        return int(self.total_land or 0) - int(self.total_land_mapping or 0)


class TemploralUploadRecord(models.Model):
    UPLOAD_STATUS_CHOICE = (
        ('INITIAL', _('Initiated')),
        ('IN_PROGRESS', _('In Progress')),
        ('LOADED', _('Loaded')),
        ('ERROR', _('Error Loaded')),
        ('CANCEL', _('Cancel by user')),
    )

    STATUS_CHOICE = (
        ('ERROR', _('contains errors')),
        ('OK_NEW', _('ok and new')),
        ('OK_OLD', _('ok to update')),
    )

    record = models.JSONField(blank=True, null=True)
    error_record = models.JSONField(blank=True, null=True)
    error_code = models.CharField(max_length=20, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True, default=None)
    land_record = models.JSONField(blank=True, null=True)
    owner_record = models.JSONField(blank=True, null=True)
    owner_record_status = models.PositiveSmallIntegerField(default=1)  # 1 nuevo 2 actualozar
    land_record_status = models.PositiveSmallIntegerField(default=1)  # 1 nuevo 2 actualozar
    upload_history = models.ForeignKey(UploadHistory, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)
    upload_status = models.CharField(max_length=20, choices=UPLOAD_STATUS_CHOICE, default='INITIAL')
    order_record = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'TMP_CARGA_REGISTROS'
        verbose_name = _('temporal upload record')
        verbose_name_plural = _('temporal upload records')

    def __str__(self):
        return f'{self.id}'


class LandOwner(AbstractAudit):
    id = models.AutoField(primary_key=True)
    ubigeo = models.ForeignKey(District, on_delete=models.CASCADE, db_column='ubigeo')
    
    code = models.CharField(max_length=50, db_column='cod_contr')
    document_type = models.ForeignKey(MasterTipoDocumentoIdentidad, on_delete=models.DO_NOTHING,blank=True, null=True, db_column='tip_doc')
    tipo_contribuyente = models.ForeignKey(MasterTipoContribuyente, on_delete=models.DO_NOTHING,blank=True, null=True)
    dni = models.CharField(max_length=20, blank=True, null=True, db_column='doc_iden')  # ToDo: Change for document
    name = models.CharField(max_length=150, blank=True, null=True, db_column='nombre')
    sec_ejec =  models.IntegerField( blank=True, null=True)
    paternal_surname = models.CharField(max_length=150, blank=True, null=True, db_column='ap_pat')
    maternal_surname = models.CharField(max_length=150, blank=True, null=True, db_column='ap_mat')
    description_owner = models.CharField(max_length=150, blank=True, null=True, db_column='contribuyente')
    phone = models.CharField(max_length=20, blank=True, null=True, db_column='telefono')
    email = models.CharField(max_length=150, blank=True, null=True, db_column='correo_electronico')
    # ToDo: This field now is OwnerAddress
    #tax_address = models.CharField(max_length=255, blank=True, null=True, db_column='dir_fiscal')
    number_lands = models.IntegerField(default=0, blank=True, null=True, db_column='numero_tierras')
    upload_history = models.ForeignKey(UploadHistory, blank=True, null=True, on_delete=models.SET_NULL,
                                       db_column='historial_carga')
    lands = models.ManyToManyField('Land', through='LandOwnerDetail', related_name='owners')
    
    class Meta:
        db_table = 'PROPIETARIO'
        #unique_together = ["ubigeo", "code"]
        verbose_name = _('land owner')
        verbose_name_plural = _('land owners')


class OwnerAddress(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.OneToOneField(LandOwner, models.CASCADE, related_name='address', blank=True, null=True)
    ubigeo = models.CharField(max_length=20, blank=True, null=True)
    uu_type = models.CharField(max_length=100, blank=True, null=True)
    cod_uu = models.CharField(max_length=100, blank=True, null=True)
    habilitacion_name = models.CharField(max_length=100, blank=True, null=True)
    cod_street = models.CharField(max_length=100, blank=True, null=True)
    street_type = models.CharField(max_length=100, blank=True, null=True)
    street_name = models.CharField(max_length=100, blank=True, null=True)
    urban_mza = models.CharField(max_length=100, blank=True, null=True)
    urban_lot_number = models.CharField(max_length=100, blank=True, null=True)
    block = models.CharField(max_length=100, blank=True, null=True)
    indoor = models.CharField(max_length=100, blank=True, null=True)
    floor = models.CharField(max_length=100, blank=True, null=True)
    km = models.CharField(max_length=100, blank=True, null=True)


class TipoMedioContacto(models.Model):
    id= models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        db_table = 'TIPO_MEDIO_CONTACTO'
        verbose_name = _('tipo de medio de contacto')
        verbose_name_plural = _('tipo de medios de contactos')


class Contacto(models.Model):
    id= models.AutoField(primary_key=True)
    contribuyente = models.ForeignKey(LandOwner, models.DO_NOTHING, related_name='contacto', blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    principal  = models.IntegerField(blank=True, null=True)
    tipo_med_contacto  = models.ForeignKey(TipoMedioContacto, models.DO_NOTHING,blank=True, null=True)

    class Meta:
        db_table = 'CONTACTO'
        verbose_name = _('contacto')
        verbose_name_plural = _('contactos')

class Domicilio(models.Model):
    id= models.AutoField(primary_key=True)
    tipo_domicilio = models.IntegerField(blank=True, null=True)
    contribuyente = models.ForeignKey(LandOwner, models.DO_NOTHING, related_name='domicilio', blank=True, null=True)
    ubigeo_domicilio = models.CharField(max_length=10, blank=True, null=True)
    des_domicilio= models.CharField(max_length=500, blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    referencia = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'DOMICILIO'
        verbose_name = _('direccion')
        verbose_name_plural = _('direcciones')

class LandBase(AbstractAudit):
    SOURCE_CHOICES = (
        ('carga_masiva', 'Carga Masiva'),
        ('asignar_lote', 'Asignar Lote'),
        ('asignar_img', 'Asignar Imagen'),
         ('mantenimiento_pre', 'Mantenimiento de Predio'),
    )
    STATUS_CHOICE = (
        (0, 'Sin Cartografia'),
        (1, 'Con cartografia (Lote)'),
        (2, 'Con cartografia (Imagen)'),
        (3, 'Inactivo'),
        (4, 'Subvaluado'),
        (5, 'Generado en gestion de resultados'),
    )
    STATUS_GAP_ANALISYS_CHOICE = (
        (0, 'Faltante'),
        (1, 'Ubicado con predio'),
        (2, 'Ubicado con punto campo'),
        (3, 'Observado'),
        
    )
    id = models.AutoField(primary_key=True)
    ubigeo = models.ForeignKey(District, on_delete=models.CASCADE, db_column='ubigeo')
    cpm = models.CharField(max_length=50, db_column='cod_pre', blank=True, null=True)
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES, blank=True, null=True, db_column='origen')
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICE, blank=True, null=True, default=0,
                                              db_column='estado')
    status_gap_analisys = models.PositiveSmallIntegerField(choices=STATUS_GAP_ANALISYS_CHOICE, blank=True, null=True, default=0,
                                              db_column='estado_analisis_brecha')
    id_land_cartographic = models.CharField(max_length=18, blank=True, null=True, help_text=_('id land cartographic'),
                                            db_column='id_predio_cartografico')
    id_plot = models.CharField(max_length=25, blank=True, null=True, help_text=_('id plot'), db_column='id_lote')
    id_lote_p = models.IntegerField( blank=True, null=True, help_text=_('id lot poligono'), db_column='id_lote_p')
    id_cartographic_img = models.CharField(max_length=26, blank=True, null=True, help_text=_('id cartographic image'),
                                           db_column='id_imagen_cartografica')
    id_object_img = models.IntegerField(blank=True, null=True, help_text=_('id object image'),
                                        db_column='id_imagen_objeto')
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, db_column='sec_ejec')
    cup = models.CharField(max_length=20, blank=True, null=True, db_column='cod_cpu')
    cod_sect = models.CharField(max_length=2, blank=True, null=True, db_column='cod_sect')
    cod_uu = models.CharField(max_length=4, blank=True, null=True, db_column='cod_uu')
    cod_mzn = models.CharField(max_length=3, blank=True, null=True, db_column='cod_mzn')
    cod_land = models.CharField(max_length=5, blank=True, null=True, db_column='cod_lote')
    cod_cuc = models.CharField(max_length=18, blank=True, null=True, db_column='cod_cuc')
    uu_type = models.CharField(max_length=2, blank=True, null=True, db_column='tipo_uu')
    habilitacion_name = models.CharField(max_length=255, blank=True, null=True, db_column='nom_uu')
    reference_name = models.CharField(max_length=255, blank=True, null=True, db_column='nom_ref')
    urban_mza = models.CharField(max_length=10, blank=True, null=True, db_column='mzn_urb')
    urban_lot_number = models.CharField(max_length=10, blank=True, null=True, db_column='lot_urb')
    cod_street = models.CharField(max_length=20, blank=True, null=True, db_column='cod_via')
    #street_type = models.CharField(max_length=20, blank=True, null=True, db_column='tip_via')
    street_type =models.ForeignKey(MasterCodeStreet,models.SET_NULL,max_length=20,  blank=True, null=True, db_column='tip_via')
    street_name = models.CharField(max_length=255, blank=True, null=True, db_column='nom_via')
    street_name_alt = models.CharField(max_length=255, blank=True, null=True, db_column='nom_alt')
    municipal_number = models.CharField(max_length=10, blank=True, null=True, db_column='num_mun')  # numero de puerta
    municipal_number_alt = models.CharField(max_length=100, blank=True, null=True, db_column='num_alt')  # numero de puerta
    block = models.CharField(max_length=6, blank=True, null=True, db_column='block')
    indoor = models.CharField(max_length=5, blank=True, null=True, db_column='interior')
    floor = models.CharField(max_length=2, blank=True, null=True, db_column='piso')
    km = models.CharField(max_length=4, blank=True, null=True, db_column='km')
    landmark = models.CharField(max_length=250, blank=True, null=True, db_column='referencia')
    municipal_address = models.CharField(max_length=255, blank=True, null=True, db_column='dir_mun')
    urban_address = models.CharField(max_length=255, blank=True, null=True, db_column='dir_urb')
    assigned_address = models.CharField(max_length=255, blank=True, null=True, db_column='dir_asig')
    longitude = models.FloatField(blank=True, null=True, db_column='coor_x')
    latitude = models.FloatField(blank=True, null=True, db_column='coor_y')
    id_aranc = models.IntegerField(blank=True, null=True, db_column='id_aranc')
    status_img = models.PositiveSmallIntegerField(blank=True, null=True, db_column='estado_imagen')
    land_area = models.FloatField(blank=True, null=True, db_column='area_terreno')
    front_length = models.FloatField(blank=True, null=True, db_column='longitud_frente')
    location_park = models.CharField(max_length=250, blank=True, null=True, db_column='ubicacion_parque')
    group_use_desc = models.CharField(max_length=50, blank=True, null=True, db_column='grupo_uso_desc')
    number_inhabitants = models.IntegerField(blank=True, null=True, db_column='cantidad_habitantes')
    classification_land_desc = models.CharField(max_length=90, blank=True, null=True,
                                                db_column='clasificacion_predio_desc')
    build_status_desc = models.CharField(max_length=120, blank=True, null=True, db_column='estado_construccion_desc')
    property_type = models.CharField(max_length=20, blank=True, null=True, db_column='tipo_predio')
    self_assessment_total = models.FloatField(blank=True, null=True, db_column='autoavaluo_total')
    condominium = models.FloatField(blank=True, null=True, db_column='condominio')
    deduction = models.FloatField(blank=True, null=True, db_column='deduccion')
    self_assessment_affection = models.FloatField(blank=True, null=True, db_column='autoavaluo_afecto')
    source_information = models.CharField(max_length=255, blank=True, null=True, db_column='fuente')
    resolution_type = models.CharField(max_length=2, blank=True, null=True, db_column='tdoc_res')
    resolution_document = models.CharField(max_length=255, blank=True, null=True, db_column='ndoc_res')
    apartment_number = models.CharField(max_length=20, blank=True, null=True, db_column='numero_departamento')
    site = models.IntegerField(blank=True, null=True, db_column='lugar')
    built_area = models.FloatField(blank=True, null=True, db_column='area_construida')
    # ToDo: Este campo sera eliminado no utilizar
    owner = models.ForeignKey(LandOwner, models.SET_NULL, blank=True, null=True, db_column='id_propietario')
    inactive_reason = models.TextField(blank=True, null=True, db_column='razon_inactivo')
    longitude_puerta = models.FloatField(blank=True, null=True, db_column='coor_x_puerta')
    latitude_puerta = models.FloatField(blank=True, null=True, db_column='coor_y_puerta') 
    id_lote_puerta =models.CharField(max_length=25, blank=True, null=True, db_column='id_lote_puerta')
    lote_urbano_puerta =models.CharField(max_length=10, blank=True, null=True) 
    manzana_urbana_puerta = models.CharField(max_length=10, blank=True, null=True) 
    class Meta:
        abstract = True


class Land(LandBase):
    upload_history = models.ForeignKey(UploadHistory, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'PREDIO'
        #unique_together = ["ubigeo", "cpm"]
        verbose_name = _('land')
        verbose_name_plural = _('lands')




class LandOwnerDetail(models.Model):
    
    land = models.ForeignKey(Land, on_delete=models.CASCADE, db_column='id_predio',related_name='predio_contribuyente')
    owner = models.ForeignKey(LandOwner, on_delete=models.CASCADE, db_column='id_propietario',related_name='contribuyentes')
    
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, db_column='sec_ejec')
    predio_codigo = models.IntegerField( blank=True, null=True) 
    cpm = models.CharField(max_length=50, db_column='cod_cpm', blank=True, null=True)
    cup = models.CharField(max_length=20, db_column='cod_cpu', blank=True, null=True)
    code = models.CharField(max_length=50, db_column='cod_contr', blank=True, null=True)
    area_terreno =  models.FloatField( blank=True, null=True)
    area_tot_terr_comun =  models.FloatField( blank=True, null=True)
    area_construida = models.FloatField( blank=True, null=True)
    area_tot_cons_comun = models.FloatField( blank=True, null=True)
    por_propiedad = models.FloatField( blank=True, null=True)
    tip_transferencia = models.ForeignKey(MasterTipoTransferencia,on_delete=models.DO_NOTHING,blank=True, null=True)
    tip_uso_predio = models.ForeignKey(MasterTipoUsoPredio,on_delete=models.DO_NOTHING,blank=True, null=True)
    tip_propiedad = models.ForeignKey(MasterTipoPropiedad,on_delete=models.DO_NOTHING,blank=True, null=True)
    fec_transferencia =models.DateField( blank=True, null=True)
    longitud_frente =models.FloatField( blank=True, null=True)
    cantidad_habitantes = models.IntegerField( blank=True, null=True)
    pre_inhabitable = models.IntegerField( blank=True, null=True)
    par_registral = models.CharField( max_length=30,blank=True, null=True)
    numero_dj = models.CharField( max_length=30,blank=True, null=True)
    fecha_dj = models.DateField(blank=True, null=True)
    usuario_auditoria = models.CharField( max_length=30,blank=True, null=True)
    ubigeo = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    estado_dj = models.IntegerField( blank=True, null=True) 
    motivo_dj = models.IntegerField( blank=True, null=True) 
    fecha =  models.DateField( blank=True, null=True, auto_now=True)
    anio_determinacion  =  models.IntegerField( blank=True, null=True,)
    fecha_adquisicion = models.DateField(blank=True, null=True)
    class Meta:
        db_table = 'PREDIO_PROPIETARIO'
        verbose_name = _('land Owner Detail')
        verbose_name_plural = _('lands Owner Detail')




class LandNivelConstruccion(models.Model):

    id = models.AutoField(primary_key=True)
    ubigeo = models.ForeignKey(District, on_delete=models.DO_NOTHING, db_column='ubigeo', related_name='nivel_ubigeo')
    land_owner_detail= models.ForeignKey(LandOwnerDetail, on_delete=models.DO_NOTHING, related_name='nivel_land_owner_detail')
    tip_nivel = models.ForeignKey(MasterTipoNivel, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='nivel_tipo_nivel')
    num_piso = models.IntegerField(blank=True, null=True)
    tip_material = models.ForeignKey(MasterTipoMaterial, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='nivel_tipo_material')
    est_conservacion = models.ForeignKey(MasterTipoEstadoConservacion, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='nivel_estado_conservacion')
    anio_construccion = models.IntegerField( blank=True, null=True)
    mes_construccion = models.IntegerField( blank=True, null=True)
    area_construida = models.FloatField( blank=True, null=True)
    area_construida_comun =models.FloatField( blank=True, null=True)
    por_area_construida_comun =models.FloatField( blank=True, null=True)
    categoria_muro_columna = models.CharField(max_length=10, blank=True, null=True)
    categoria_puerta_ventana = models.CharField(max_length=10, blank=True, null=True)
    categoria_revestimiento = models.CharField(max_length=10, blank=True, null=True)
    categoria_bano = models.CharField(max_length=10, blank=True, null=True)
    categoria_inst_electrica_sanita = models.CharField(max_length=10, blank=True, null=True)
    estado = models.IntegerField( blank=True, null=True)

    class Meta:
        db_table = 'PREDIO_NIVEL_CONSTRUCCION'
        verbose_name = _('nivel de construccion')
        verbose_name_plural = _('niveles de construccion')

class OwnerDeuda(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(LandOwner, on_delete=models.DO_NOTHING, blank=True, null=True)
    tiene_deuda  = models.IntegerField( blank=True, null=True)
    anio = models.IntegerField( blank=True, null=True)
    
    class Meta:
        db_table = 'PROPIETARIO_DEUDA'
        verbose_name = _('nivel de construccion')
        verbose_name_plural = _('niveles de construccion')

class LandAudit(LandBase):
    SOURCE_CHANGE_CHOICES = (
        ('carga_masiva', 'Carga Masiva'),
        ('asignar_lote', 'Asignar Lote'),
        ('asignar_img', 'Asignar Imagen'),
    )

    TYPE_CHOICES = (
        ('editar', 'Editar Registro'),
        ('inactivar', 'Inactivar Registro')
    )
    id_reference = models.IntegerField()
    source_change = models.CharField(max_length=50, choices=SOURCE_CHANGE_CHOICES, blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, blank=True, null=True)

    class Meta:
        db_table = 'PREDIO_AUDITORIA'
        verbose_name = _('land audit')
        verbose_name_plural = _('land audits')
