# Generated by Django 3.2.19 on 2023-11-14 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('land_inspections', '0006_auto_20231114_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='inspection_upload',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='land_inspections.landinspectionupload'),
        ),
    ]