# Generated by Django 2.0.2 on 2018-05-31 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honoradar', '0010_auto_20180526_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacollection',
            name='Suspiciousentry',
            field=models.CharField(blank=True, choices=[('Ok', 'Ok'), ('Weird', 'Weird')], default='Ok', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='medium',
            name='Suspiciousmedium',
            field=models.CharField(blank=True, choices=[('Ok', 'Ok'), ('Weird', 'Weird')], default='Ok', max_length=20, null=True),
        ),
    ]