# Generated by Django 3.1.14 on 2022-07-31 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GisCatalog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'GIS catalog',
                'verbose_name_plural': 'GIS catalogs',
                'db_table': 'CATALOGO_GIS',
            },
        ),
        migrations.CreateModel(
            name='GisService',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, default=None, null=True)),
                ('catalog', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='gis.giscatalog')),
            ],
            options={
                'verbose_name': 'GIS service',
                'verbose_name_plural': 'GIS services',
                'db_table': 'SERVICIO_GIS',
            },
        ),
        migrations.CreateModel(
            name='GisCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='gis.giscategory')),
            ],
            options={
                'verbose_name': 'GIS category',
                'verbose_name_plural': 'GIS categories',
                'db_table': 'CATEGORIA_GIS',
            },
        ),
        migrations.AddField(
            model_name='giscatalog',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gis.giscategory'),
        ),
    ]
