# Generated by Django 5.0.3 on 2024-05-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_housemodel_embeded_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemodel',
            name='embeded_url',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='housemodel',
            name='latitude',
            field=models.FloatField(default=''),
        ),
        migrations.AlterField(
            model_name='housemodel',
            name='longitude',
            field=models.FloatField(default=''),
        ),
    ]
