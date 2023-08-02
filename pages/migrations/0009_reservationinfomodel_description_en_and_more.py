# Generated by Django 4.2.3 on 2023-07-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_reservationinfomodel_reservationmodel_name_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationinfomodel',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='reservationinfomodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='reservationinfomodel',
            name='discount_title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='discount_title'),
        ),
        migrations.AddField(
            model_name='reservationinfomodel',
            name='discount_title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='discount_title'),
        ),
        migrations.AddField(
            model_name='reservationinfomodel',
            name='sub_title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='sub_title'),
        ),
        migrations.AddField(
            model_name='reservationinfomodel',
            name='sub_title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='sub_title'),
        ),
    ]