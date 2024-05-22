# Generated by Django 4.1 on 2022-09-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_platmenuenfant_origin_viande_platmenuenfant_prix_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DessertEnfant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_et_ou_prix', models.CharField(max_length=200)),
                ('prix', models.FloatField(default=0)),
                ('origin_viande', models.CharField(blank=True, max_length=200)),
                ('commentaire', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
