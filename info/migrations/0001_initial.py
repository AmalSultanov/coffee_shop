# Generated by Django 4.2.3 on 2023-07-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_image', verbose_name='image')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_image', verbose_name='image')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('sub_title', models.CharField(max_length=100, verbose_name='sub_title')),
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
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='client_image', verbose_name='image')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('profession', models.CharField(max_length=100, verbose_name='profession')),
                ('description', models.TextField(verbose_name='left_description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'clients',
            },
        ),
        migrations.CreateModel(
            name='PreTestimonialModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('sub_title', models.CharField(max_length=100, verbose_name='sub_title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'pre_testimonial',
                'verbose_name_plural': 'pre_testimonials',
            },
        ),
        migrations.CreateModel(
            name='TestimonialImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testimonial_image', verbose_name='image')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
    ]
