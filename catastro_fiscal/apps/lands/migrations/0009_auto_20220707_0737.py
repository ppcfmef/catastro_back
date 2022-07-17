# Generated by Django 3.1.14 on 2022-07-07 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0008_auto_20220707_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owneraddress',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='lands.landowner'),
        ),
    ]
