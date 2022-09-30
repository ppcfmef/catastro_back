# Generated by Django 3.2.15 on 2022-09-30 09:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0020_auto_20220902_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='landowner',
            name='created_by',
            field=models.CharField(blank=True, help_text='username that created the record', max_length=100, null=True, verbose_name='username created'),
        ),
        migrations.AddField(
            model_name='landowner',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='record creation date', verbose_name='creation date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landowner',
            name='update_by',
            field=models.CharField(blank=True, help_text='username that updated the record', max_length=100, null=True, verbose_name='username updated'),
        ),
        migrations.AddField(
            model_name='landowner',
            name='update_date',
            field=models.DateTimeField(auto_now=True, help_text='record update date', verbose_name='update date'),
        ),
    ]
