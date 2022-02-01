from django.db import models


class Navigation(models.Model):
    """Navigation model: Store a aplication menu"""
    TYPE_CHOICES = (
        ('group', 'Group'),
        ('collapsable', 'Collapsable'),
        ('basic', 'Basic'),
    )
    id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', models.SET_NULL, related_name='children', blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    icon = models.CharField(max_length=200)
    link = models.CharField(max_length=200, blank=True, null=True)
    order = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'MENU'
        ordering = ['order']

    def __str__(self):
        if not self.parent:
            return self.title
        if not self.parent.parent:
            return f'{self.parent.title} > {self.title}'
        return f'{self.parent.parent.title} > {self.parent.title} > {self.title}'