# Generated by Django 3.2.16 on 2023-04-19 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0038_auto_20230419_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landowner',
            name='dni',
            field=models.CharField(blank=True, db_column='doc_iden', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='landowner',
            name='document_type',
            field=models.CharField(blank=True, db_column='tip_doc', max_length=2, null=True),
        ),
    ]
