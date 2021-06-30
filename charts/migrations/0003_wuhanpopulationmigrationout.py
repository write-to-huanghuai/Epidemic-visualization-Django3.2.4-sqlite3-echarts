# Generated by Django 3.2.4 on 2021-06-27 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0002_hubeiprovincehistoryepidemicdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='WuhanPopulationMigrationOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_code', models.IntegerField()),
                ('city_name', models.CharField(max_length=20)),
                ('city_rate_out', models.FloatField()),
                ('city_rate_in', models.FloatField()),
            ],
        ),
    ]
