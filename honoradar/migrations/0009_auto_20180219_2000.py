# Generated by Django 2.0 on 2018-02-19 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honoradar', '0008_remove_medium_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacollection',
            name='LohnProAuftrag',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='MinutenProAudio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='MinutenProVideo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='ProductType',
            field=models.CharField(default='Text', max_length=200),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='ZeichenProArtikel',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='Zeitaufwand',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='arbeitszeit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='position',
            field=models.CharField(default='Redakteur', max_length=200),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='stundenProTag',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='tageProMonat',
            field=models.IntegerField(default=0),
        ),
    ]
