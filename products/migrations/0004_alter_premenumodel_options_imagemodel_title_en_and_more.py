# Generated by Django 4.2.3 on 2023-07-17 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='premenumodel',
            options={'verbose_name': 'pre menu', 'verbose_name_plural': 'pre menus'},
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='premenumodel',
            name='option1_en',
            field=models.CharField(max_length=100, null=True, verbose_name='option1'),
        ),
        migrations.AddField(
            model_name='premenumodel',
            name='option1_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='option1'),
        ),
        migrations.AddField(
            model_name='premenumodel',
            name='option2_en',
            field=models.CharField(max_length=100, null=True, verbose_name='option2'),
        ),
        migrations.AddField(
            model_name='premenumodel',
            name='option2_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='option2'),
        ),
        migrations.AddField(
            model_name='premenumodel',
            name='sub_title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='sub_title'),
        ),
        migrations.AddField(
            model_name='premenumodel',
            name='sub_title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='sub_title'),
        ),
        migrations.AddField(
            model_name='premenumodel',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='premenumodel',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
    ]
