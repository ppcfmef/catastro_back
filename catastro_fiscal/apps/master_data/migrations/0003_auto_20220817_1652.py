# Generated by Django 3.1.14 on 2022-08-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0002_mastercodestreet_masterpropertytype_masterside_mastertypeurbanunit'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterResolutionType',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='key id')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('description', models.CharField(max_length=150, verbose_name='description')),
                ('short_name', models.CharField(max_length=100, verbose_name='short name')),
            ],
            options={
                'verbose_name': 'Resolution Type',
                'verbose_name_plural': 'Resolution Type',
                'db_table': 'M_TDOC_RES',
            },
        ),
        migrations.AlterModelOptions(
            name='mastercodestreet',
            options={'verbose_name': 'Code Street', 'verbose_name_plural': 'Code Street'},
        ),
        migrations.AlterModelOptions(
            name='masterpropertytype',
            options={'verbose_name': 'Property Type', 'verbose_name_plural': 'Property Type'},
        ),
        migrations.AlterModelOptions(
            name='masterside',
            options={'verbose_name': 'Side', 'verbose_name_plural': 'Side'},
        ),
        migrations.AlterModelOptions(
            name='mastertypeurbanunit',
            options={'verbose_name': 'Type Urban Unit', 'verbose_name_plural': 'Type Urban Unit'},
        ),
    ]