# Generated by Django 4.2.3 on 2023-07-22 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_rename_type_productmodel_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.productcategorymodel', verbose_name='category'),
        ),
    ]
