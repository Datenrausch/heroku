# Generated by Django 2.0.2 on 2018-05-26 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honoradar', '0007_auto_20180526_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AddField(
            model_name='medium',
            name='UpDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]