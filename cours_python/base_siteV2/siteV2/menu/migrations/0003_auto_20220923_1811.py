# Generated by Django 3.2.15 on 2022-09-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_delete_a_entrees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nouveaux_Plats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_plat', models.CharField(max_length=200)),
                ('prix', models.FloatField(default=0)),
                ('origin_viande', models.CharField(blank=True, max_length=200)),
                ('commentaire', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='infosMenu',
        ),
    ]
