# Generated by Django 3.0.3 on 2021-08-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sondage', '0006_auto_20210828_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='person',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
