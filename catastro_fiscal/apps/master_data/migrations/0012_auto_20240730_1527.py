# Generated by Django 3.2.19 on 2024-07-30 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0011_auto_20240627_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterpropertytype',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='masterpropertytype',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='name'),
        ),
    ]