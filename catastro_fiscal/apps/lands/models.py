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
    dni = models.CharField(max_length=20)
    name = models.CharField(max_length=150)
    paternal_surname = models.CharField(max_length=150, blank=True, null=True)
    maternal_surname = models.CharField(max_length=150, blank=True, null=True)
    tax_address = models.CharField(max_length=255, blank=True, null=True)
    numberLands = models.IntegerField(default=0)

    class Meta:
        db_table = 'PROPIETARIO'
        verbose_name = _('land owner')
        verbose_name_plural = _('land owners')


class Land(models.Model):
    id = models.AutoField(primary_key=True)
    cup = models.CharField(max_length=50)
    cpm = models.CharField(max_length=50, blank=True, null=True)
    habilitacion_name = models.CharField(max_length=150, blank=True, null=True)
    steet_name = models.CharField(max_length=150, blank=True, null=True)
    urban_mza = models.CharField(max_length=50, blank=True, null=True)
    urban_lot_number = models.CharField(max_length=150, blank=True, null=True)
    road_block_number = models.IntegerField(blank=True, null=True)
    site = models.IntegerField(blank=True, null=True)
    municipal_number = models.IntegerField(blank=True, null=True)
    alternate_number = models.IntegerField(blank=True, null=True)
    dpto_number = models.IntegerField(blank=True, null=True)
    indoor = models.CharField(max_length=50, blank=True, null=True)
    block = models.CharField(max_length=150, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    land_area = models.FloatField(blank=True, null=True)
    built_area = models.FloatField(blank=True, null=True)
    owner = models.ForeignKey(LandOwner, models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'PREDIO'
        verbose_name = _('land')
        verbose_name_plural = _('land')
