# Generated by Django 4.2.3 on 2023-07-16 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AboutModel',
        ),
        migrations.DeleteModel(
            name='BannerModel',
        ),
        migrations.DeleteModel(
            name='ContactModel',
        ),
    ]