# Generated by Django 4.2.3 on 2023-07-16 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_image', verbose_name='image')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('left_title', models.CharField(max_length=100, verbose_name='left_title')),
                ('left_description', models.TextField(verbose_name='left_description')),
                ('right_title', models.CharField(max_length=100, verbose_name='right_title')),
                ('right_description', models.TextField(verbose_name='right_description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'about',
                'verbose_name_plural': 'about',
            },
        ),
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home_banners', verbose_name='image')),
                ('upper_title', models.CharField(max_length=100, verbose_name='upper_title')),
                ('middle_title', models.CharField(max_length=100, verbose_name='middle_title')),
                ('lower_title', models.CharField(max_length=100, verbose_name='lower_title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
            },
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('subject', models.CharField(max_length=100, verbose_name='subject')),
                ('message', models.TextField(verbose_name='message')),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
    ]
