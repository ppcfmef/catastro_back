from django.db import models
from django.utils.translation import gettext_lazy as _


class Institution(models.Model):
    name = models.CharField(_('name'), max_length=150)

    class Meta:
        db_table = 'INSTITUCION'

    def __str__(self):
        return self.name
