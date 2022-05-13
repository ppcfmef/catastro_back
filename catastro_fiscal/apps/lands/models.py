from django.db import models
from django.utils.translation import gettext_lazy as _


class UploadHistory(models.Model):
    STATUS_CHOICE = (
        ('INITIAL', _('Initiated')),
        ('IN_PROGRESS', _('In Progress')),
        ('LOADED', _('Loaded')),
    )

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
