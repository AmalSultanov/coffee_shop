# Generated by Django 4.2.3 on 2023-08-01 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_productcategorymodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.CharField(max_length=10, verbose_name='price'),
        ),
    ]
