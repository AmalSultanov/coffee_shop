# Generated by Django 4.2.3 on 2023-07-26 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_reservationinfomodel_description_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
    ]
