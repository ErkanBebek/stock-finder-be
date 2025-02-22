# Generated by Django 5.0.6 on 2024-06-28 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hisse_senedi_adi', models.TextField()),
                ('son_fiyat', models.FloatField(blank=True, null=True)),
                ('kar_degisim', models.FloatField(blank=True, null=True)),
                ('son_donem_kar', models.FloatField(blank=True, null=True)),
                ('gecen_sene_kar', models.FloatField(blank=True, null=True)),
                ('son_donem', models.TextField()),
                ('fd_favok', models.FloatField(blank=True, null=True)),
                ('sektorun_fd_favok_ortalamasi', models.FloatField(blank=True, null=True)),
                ('fd_satislar', models.FloatField(blank=True, null=True)),
                ('sektorun_fd_satislar_ortalamasi', models.FloatField(blank=True, null=True)),
                ('fk', models.FloatField(blank=True, null=True)),
                ('sektorun_fk_ortalamasi', models.FloatField(blank=True, null=True)),
                ('pd_dd', models.FloatField(blank=True, null=True)),
                ('sektorun_pd_dd_ortalamasi', models.FloatField(blank=True, null=True)),
                ('sektor', models.TextField()),
            ],
            options={
                'db_table': 'tr_stock',
            },
        ),
    ]
