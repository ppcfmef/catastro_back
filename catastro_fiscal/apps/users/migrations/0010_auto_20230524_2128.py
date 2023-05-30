# Generated by Django 3.2.19 on 2023-05-24 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20221127_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_mobile_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this mobile apps.', verbose_name='mobile staff status'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_web_staff',
            field=models.BooleanField(default=True, help_text='Designates whether the user can log into this web platform', verbose_name='web staff status'),
        ),
    ]