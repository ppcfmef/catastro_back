# Generated by Django 3.1.14 on 2022-02-06 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220206_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(through='users.RolePermission', to='users.Permission', verbose_name='permissions'),
        ),
    ]
