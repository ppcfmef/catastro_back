from django.db import models
from django.utils.translation import gettext_lazy as _

UPLOAD_STATUS = (
        ('INITIAL', _('Initiated')),
        ('IN_PROGRESS', _('In Progress')),
        ('LOADED', _('Loaded')),
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
    upload_history = models.ForeignKey(UploadHistory, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=UPLOAD_STATUS_CHOICE)
    upload_status = models.CharField(max_length=20, choices=UPLOAD_STATUS_CHOICE, default='INITIAL')

    class Meta:
        db_table = 'TMP_CARGA_REGISTROS'
        verbose_name = _('temporal upload redord')
        verbose_name_plural = _('temporal upload redords')

    def __str__(self):
        return f'{self.id}'


class LandOwner(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    document_type = models.CharField(max_length=2, blank=True, null=True)
    dni = models.CharField(max_length=20, unique=True)  # ToDo: Change for document
    name = models.CharField(max_length=150)
    paternal_surname = models.CharField(max_length=150, blank=True, null=True)
    maternal_surname = models.CharField(max_length=150, blank=True, null=True)
    description_owner = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    tax_address = models.CharField(max_length=255, blank=True, null=True)  # ToDo: This field now is OwnerAddress
    number_lands = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'PROPIETARIO'
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


class Land(models.Model):
    id = models.AutoField(primary_key=True)
    id_land_cartographic = models.CharField(max_length=18, blank=True, null=True, help_text=_('id land cartographic'))
    cpm = models.CharField(max_length=100, blank=True, null=True)
    sec_ejec = models.CharField(max_length=6, blank=True, null=True)
    ubigeo = models.CharField(max_length=6, blank=True, null=True)
    cup = models.CharField(max_length=15, blank=True, null=True)
    cod_sect = models.CharField(max_length=2, blank=True, null=True)
    cod_uu = models.CharField(max_length=4, blank=True, null=True)
    cod_mzn = models.CharField(max_length=3, blank=True, null=True)
    cod_land = models.CharField(max_length=5, blank=True, null=True)
    cod_cuc = models.CharField(max_length=18, blank=True, null=True)
    uu_type = models.CharField(max_length=2, blank=True, null=True)
    habilitacion_name = models.CharField(max_length=255, blank=True, null=True)
    reference_name = models.CharField(max_length=255, blank=True, null=True)
    urban_mza = models.CharField(max_length=10, blank=True, null=True)
    urban_lot_number = models.CharField(max_length=10, blank=True, null=True)
    cod_street = models.CharField(max_length=20, blank=True, null=True)
    street_type = models.CharField(max_length=20, blank=True, null=True)
    street_name = models.CharField(max_length=255, blank=True, null=True)
    street_name_alt = models.CharField(max_length=255, blank=True, null=True)
    municipal_number = models.CharField(max_length=6, blank=True, null=True)
    block = models.CharField(max_length=6, blank=True, null=True)
    indoor = models.CharField(max_length=5, blank=True, null=True)
    floor = models.CharField(max_length=2, blank=True, null=True)
    km = models.CharField(max_length=4, blank=True, null=True)
    landmark = models.CharField(max_length=250, blank=True, null=True)
    municipal_address = models.CharField(max_length=255, blank=True, null=True)
    urban_address = models.CharField(max_length=255, blank=True, null=True)
    assigned_address = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    id_aranc = models.IntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    land_area = models.FloatField(blank=True, null=True)
    front_length = models.FloatField(blank=True, null=True)
    location_park = models.CharField(max_length=250, blank=True, null=True)
    group_use_desc = models.CharField(max_length=50, blank=True, null=True)
    number_inhabitants = models.IntegerField(blank=True, null=True)
    classification_land_desc = models.CharField(max_length=90, blank=True, null=True)
    build_status_desc = models.CharField(max_length=120, blank=True, null=True)
    property_type = models.CharField(max_length=20, blank=True, null=True)
    self_assessment_total = models.FloatField(blank=True, null=True)
    condominium = models.FloatField(blank=True, null=True)
    deduction = models.FloatField(blank=True, null=True)
    self_assessment_affection = models.FloatField(blank=True, null=True)
    source_information = models.CharField(max_length=255, blank=True, null=True)
    resolution_type = models.CharField(max_length=2, blank=True, null=True)
    resolution_document = models.CharField(max_length=255, blank=True, null=True)
    dpto_number = models.IntegerField(blank=True, null=True)
    site = models.IntegerField(blank=True, null=True)
    built_area = models.FloatField(blank=True, null=True)
    owner = models.ForeignKey(LandOwner, models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'PREDIO'
        verbose_name = _('land')
        verbose_name_plural = _('land')
