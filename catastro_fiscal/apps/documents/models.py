from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        related_name='children',
        on_delete=models.CASCADE,
        null=True, blank=True, default=None,
    )

    class Meta:
        db_table = 'CATEGORIA'
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return f'{self.name}'


class Document(models.Model):
    class DocumentType(models.IntegerChoices):
        USER_MANUAL = 1, _('User manual')
        VIDEO_TUTORIAL = 2, _('Video tutorial')
        FAQ = 3, _('FAQ')

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.PositiveSmallIntegerField(choices=DocumentType.choices, default=None)
    category = models.ForeignKey('documents.Category', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    url = models.URLField(null=True, blank=True, default=None)
    thumbnail = models.FileField(upload_to='documents', null=True, blank=True, default=None)

    class Meta:
        db_table = 'DOCUMENTO'
        verbose_name = _('document')
        verbose_name_plural = _('documents')

    def __str__(self):
        return f'{self.title}'
