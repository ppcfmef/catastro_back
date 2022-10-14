# Generated by Django 3.2.15 on 2022-10-13 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0023_alter_landowner_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='upload_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lands.uploadhistory'),
        ),
        migrations.AddField(
            model_name='landowner',
            name='upload_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lands.uploadhistory'),
        ),
    ]
