# Generated by Django 2.0.2 on 2018-06-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honoradar', '0012_datacollection_gegendarstellung'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medium',
            name='fairness',
            field=models.CharField(blank=True, choices=[('keineAngabe', 'keineAngabe'), ('Ja', 'Ja'), ('Hoelle', 'Hoelle'), ('Himmel', 'Himmel'), ('HoelleJa', 'HoelleJa'), ('HimmelJa', 'HimmelJa')], default='', max_length=20, null=True),
        ),
    ]
