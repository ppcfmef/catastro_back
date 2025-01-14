# Generated by Django 3.2.19 on 2024-06-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0072_auto_20240624_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='landownerdetail',
            old_name='usuario_creacion',
            new_name='usuario_auditoria',
        ),
        migrations.RemoveField(
            model_name='landownerdetail',
            name='estado',
        ),
        migrations.AddField(
            model_name='domicilio',
            name='referencia',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='domicilio',
            name='tipo_domicilio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landownerdetail',
            name='estado_dj',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landownerdetail',
            name='motivo_dj',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landownerdetail',
            name='predio_codigo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landownerdetail',
            name='sec_ejec',
            field=models.CharField(blank=True, db_column='sec_ejec', max_length=6, null=True),
        ),
    ]
