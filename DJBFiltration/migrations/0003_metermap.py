# Generated by Django 4.2.7 on 2024-07-17 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DJBFiltration', '0002_impurest_maxruntime_minruntime_purest_runtimedetail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metermap',
            fields=[
                ('metergroupid', models.BigIntegerField(db_column='MeterGroupID', primary_key=True, serialize=False)),
                ('metergroupname', models.CharField(blank=True, db_column='MetergroupName', max_length=45, null=True)),
                ('subscriberid', models.BigIntegerField(db_column='SubscriberID')),
            ],
            options={
                'db_table': 'meter_map',
                'managed': False,
            },
        ),
    ]