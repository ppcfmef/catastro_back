# Generated by Django 3.2.19 on 2024-07-30 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0078_rename_tipo_med_contacto_contacto_tip_med_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landnivelconstruccion',
            name='estado',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='landnivelconstruccion',
            name='land_owner_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='niveles_construccion', to='lands.landownerdetail'),
        ),
        migrations.AlterField(
            model_name='landownerdetail',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
