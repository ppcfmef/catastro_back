# Generated by Django 3.1.14 on 2022-07-07 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0007_auto_20220513_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='landowner',
            name='description_owner',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='landowner',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='landowner',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='OwnerAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ubigeo', models.CharField(blank=True, max_length=20, null=True)),
                ('uu_type', models.CharField(blank=True, max_length=100, null=True)),
                ('cod_uu', models.CharField(blank=True, max_length=100, null=True)),
                ('habilitacion_name', models.CharField(blank=True, max_length=100, null=True)),
                ('cod_street', models.CharField(blank=True, max_length=100, null=True)),
                ('street_type', models.CharField(blank=True, max_length=100, null=True)),
                ('street_name', models.CharField(blank=True, max_length=100, null=True)),
                ('urban_mza', models.CharField(blank=True, max_length=100, null=True)),
                ('urban_lot_number', models.CharField(blank=True, max_length=100, null=True)),
                ('block', models.CharField(blank=True, max_length=100, null=True)),
                ('indoor', models.CharField(blank=True, max_length=100, null=True)),
                ('floor', models.CharField(blank=True, max_length=100, null=True)),
                ('km', models.CharField(blank=True, max_length=100, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='lands.landowner')),
            ],
        ),
    ]
