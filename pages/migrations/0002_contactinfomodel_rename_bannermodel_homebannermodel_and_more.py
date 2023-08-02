# Generated by Django 4.2.3 on 2023-07-17 16:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('sub_title', models.CharField(max_length=100, verbose_name='sub_title')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
                ('phone', models.PositiveIntegerField(max_length=100, verbose_name='phone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'contact_info',
                'verbose_name_plural': 'contacts_info',
            },
        ),
        migrations.RenameModel(
            old_name='BannerModel',
            new_name='HomeBannerModel',
        ),
        migrations.DeleteModel(
            name='AboutModel',
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created_at'),
            preserve_default=False,
        ),
    ]
