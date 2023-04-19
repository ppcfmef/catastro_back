from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import AbstractAudit
from apps.places.models import District

UPLOAD_STATUS = (
    ('INITIAL', _('Initiated')),
    ('IN_PROGRESS', _('In Progress')),
    ('LOADED', _('Loaded')),
    ('ERROR', _('Error Loaded')),
    ('CANCEL', _('Cancel by user')),
)


class UploadHistory(models.Model):
    STATUS_CHOICE = UPLOAD_STATUS

    APPROVED_STATUS_CHOICE = (
        ('NOT_REQUIRED', _('Not required')),
        ('PENDING', _('Pending approval')),
        ('APPRIVING', _('In approval process')),
        ('APPROVED', _('Approved')),
    )
    id = models.AutoField(primary_key=True)
    file_upload = models.FileField(upload_to='lands/registry')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, default=None)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='INITIAL')
    approved_status = models.CharField(max_length=20, choices=APPROVED_STATUS_CHOICE, default='NOT_REQUIRED')
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
    UPLOAD_STATUS_CHOICE = UPLOAD_STATUS

    STATUS_CHOICE = (
        ('ERROR', _('contains errors')),
        ('OK_NEW', _('ok and new')),
        ('OK_OLD', _('ok to update')),
    )

    record = models.JSONField(blank=True, null=True)
    error_record = models.JSONField(blank=True, null=True)
    error_code = models.CharField(max_length=20, blank=True, null=True)
    land_record = models.JSONField(blank=True, null=True)
    owner_record = models.JSONField(blank=True, null=True)
    owner_record_status = models.PositiveSmallIntegerField(default=1)  # 1 nuevo 2 actualozar
    land_record_status = models.PositiveSmallIntegerField(default=1)  # 1 nuevo 2 actualozar
    upload_history = models.ForeignKey(UploadHistory, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)
    upload_status = models.CharField(max_length=20, choices=UPLOAD_STATUS_CHOICE, default='INITIAL')

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
    document_type = models.CharField(max_length=2, blank=True, null=True, db_column='tip_doc')
    dni = models.CharField(max_length=20, blank=True, null=True, db_column='doc_iden')  # ToDo: Change for document
    name = models.CharField(max_length=150, blank=True, null=True, db_column='nombre')
    paternal_surname = models.CharField(max_length=150, blank=True, null=True, db_column='ap_pat')
    maternal_surname = models.CharField(max_length=150, blank=True, null=True, db_column='ap_mat')
    description_owner = models.CharField(max_length=150, blank=True, null=True, db_column='contribuyente')
    phone = models.CharField(max_length=20, blank=True, null=True, db_column='telefono')
    email = models.CharField(max_length=150, blank=True, null=True, db_column='correo_electronico')
    # ToDo: This field now is OwnerAddress
    tax_address = models.CharField(max_length=255, blank=True, null=True, db_column='dir_fiscal')
    number_lands = models.IntegerField(default=0, blank=True, null=True, db_column='numero_tierras')
    upload_history = models.ForeignKey(UploadHistory, blank=True, null=True, on_delete=models.SET_NULL,
                                       db_column='historial_carga')
    lands = models.ManyToManyField('Land', through='LandOwnerDetail', related_name='owners')

    class Meta:
        db_table = 'PROPIETARIO'
        unique_together = ["ubigeo", "code"]
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


class LandBase(AbstractAudit):
    SOURCE_CHOICES = (
        ('carga_masiva', 'Carga Masiva'),
        ('asignar_lote', 'Asignar Lote'),
        ('asignar_img', 'Asignar Imagen'),
    )
    STATUS_CHOICE = (
        (0, 'Sin Cartografia'),
        (1, 'Con cartografia (Lote)'),
        (2, 'Con cartografia (Imagen)'),
        (3, 'Inactivo'),
    )
    id = models.AutoField(primary_key=True)
    ubigeo = models.ForeignKey(District, on_delete=models.CASCADE, db_column='ubigeo')
    cpm = models.CharField(max_length=15, db_column='cod_pre')
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES, blank=True, null=True, db_column='origen')
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICE, blank=True, null=True, default=0,
                                              db_column='estado')
    id_land_cartographic = models.CharField(max_length=18, blank=True, null=True, help_text=_('id land cartographic'),
                                            db_column='id_predio_cartografico')
    id_plot = models.CharField(max_length=25, blank=True, null=True, help_text=_('id plot'), db_column='id_lote')
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
    street_type = models.CharField(max_length=20, blank=True, null=True, db_column='tip_via')
    street_name = models.CharField(max_length=255, blank=True, null=True, db_column='nom_via')
    street_name_alt = models.CharField(max_length=255, blank=True, null=True, db_column='nom_alt')
    municipal_number = models.CharField(max_length=6, blank=True, null=True, db_column='num_mun')  # numero de puerta
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

    class Meta:
        abstract = True


class Land(LandBase):
    upload_history = models.ForeignKey(UploadHistory, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'PREDIO'
        unique_together = ["ubigeo", "cpm"]
        verbose_name = _('land')
        verbose_name_plural = _('lands')


class LandOwnerDetail(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE, db_column='id_predio')
    owner = models.ForeignKey(LandOwner, on_delete=models.CASCADE, db_column='id_propietario')
    ubigeo = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True, db_column='ubigeo')

    class Meta:
        db_table = 'PREDIO_PROPIETARIO'
        verbose_name = _('land Owner Detail')
        verbose_name_plural = _('lands Owner Detail')


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
