# Generated by Django 2.0.2 on 2018-05-31 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honoradar', '0011_auto_20180531_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacollection',
            name='Gegendarstellung',
            field=models.TextField(blank=True, default=None, max_length=600, null=True),
        ),
    ]