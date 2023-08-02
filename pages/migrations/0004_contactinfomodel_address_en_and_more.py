# Generated by Django 4.2.3 on 2023-07-17 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_contactinfomodel_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfomodel',
            name='address_en',
            field=models.CharField(max_length=100, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='contactinfomodel',
            name='address_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='contactinfomodel',
            name='sub_title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='sub_title'),
        ),
        migrations.AddField(
            model_name='contactinfomodel',
            name='sub_title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='sub_title'),
        ),
        migrations.AddField(
            model_name='contactinfomodel',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='contactinfomodel',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='homebannermodel',
            name='lower_title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='lower_title'),
        ),
        migrations.AddField(
            model_name='homebannermodel',
            name='lower_title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='lower_title'),
        ),
        migrations.AddField(
            model_name='homebannermodel',
            name='middle_title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='middle_title'),
        ),
        migrations.AddField(
            model_name='homebannermodel',
            name='middle_title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='middle_title'),
        ),
        migrations.AddField(
            model_name='homebannermodel',
            name='upper_title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='upper_title'),
        ),
        migrations.AddField(
            model_name='homebannermodel',
            name='upper_title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='upper_title'),
        ),
    ]