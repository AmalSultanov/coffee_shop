# Generated by Django 4.2.3 on 2023-07-31 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_delete_imagemodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategorymodel',
            options={'verbose_name': 'product category', 'verbose_name_plural': 'product categories'},
        ),
    ]
