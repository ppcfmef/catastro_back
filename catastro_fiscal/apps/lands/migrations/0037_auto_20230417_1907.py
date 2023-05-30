# Generated by Django 3.2.16 on 2023-04-17 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20221127_0042'),
        ('lands', '0036_auto_20221127_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandOwnerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land', models.ForeignKey(db_column='id_predio', on_delete=django.db.models.deletion.CASCADE, to='lands.land')),
                ('owner', models.ForeignKey(db_column='id_propietario', on_delete=django.db.models.deletion.CASCADE, to='lands.landowner')),
                ('ubigeo', models.ForeignKey(blank=True, db_column='ubigeo', null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.district')),
            ],
            options={
                'verbose_name': 'land Owner Detail',
                'verbose_name_plural': 'lands Owner Detail',
                'db_table': 'PREDIO_PROPIETARIO',
            },
        ),
        migrations.AddField(
            model_name='landowner',
            name='lands',
            field=models.ManyToManyField(related_name='owners', through='lands.LandOwnerDetail', to='lands.Land'),
        ),
    ]