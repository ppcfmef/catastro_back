# Generated by Django 3.2.19 on 2024-09-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land_inspections', '0009_auto_20240912_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='landfacility',
            name='piso',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]