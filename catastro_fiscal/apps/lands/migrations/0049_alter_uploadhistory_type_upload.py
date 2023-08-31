# Generated by Django 3.2.19 on 2023-08-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0048_alter_uploadhistory_type_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadhistory',
            name='type_upload',
            field=models.CharField(choices=[('TB_PREDIO', 'TB_PREDIO'), ('RT_CONTRIBUYENTE', 'RT_CONTRIBUYENTE'), ('RT_MARCO_PREDIO', 'RT_MARCOPREDIO'), ('RT_ARANCEL', 'RT_ARANCEL'), ('RT_PREDIO_DATO', 'RT_PREDIO_DATO'), ('RT_PREDIO_CARACT', 'RT_PREDIO_CARACT'), ('RT_RECAUDACION', 'RT_RECAUDACION'), ('RT_DEUDA', 'RT_DEUDA'), ('RT_EMISION', 'RT_EMISION'), ('RT_BIMPONIBLE', 'RT_BIMPONIBLE'), ('RT_ALICUOTA', 'RT_ALICUOTA'), ('RT_AMNCONTRIBUYENTE', 'RT_AMNCONTRIBUYENTE'), ('RT_AMNMUNICIPAL', 'RT_AMNMUNICIPAL'), ('RT_VAREM_MUN', 'RT_VAREM_MUN')], default='TB_PREDIO', max_length=50),
        ),
    ]
