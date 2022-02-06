# Generated by Django 3.1.14 on 2022-02-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_permission_permissionnavigation_permissiontype_rolepermission'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permissiontype',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='permissiontype',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='order'),
            preserve_default=False,
        ),
    ]