# Generated by Django 4.1 on 2022-09-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_entree_origin_viande_alter_plat_origin_viande'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion_Plat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prix', models.FloatField(default=0)),
                ('origin_viande', models.CharField(blank=True, max_length=200)),
                ('commentaire', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='dessert',
            name='commentaire',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='entree',
            name='commentaire',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='plat',
            name='commentaire',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
