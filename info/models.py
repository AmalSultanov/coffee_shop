from django.db import models
from django.utils.translation import gettext_lazy as _


class AboutModel(models.Model):
    image = models.ImageField(upload_to='about_image',
                              verbose_name=_('image'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    sub_title = models.CharField(max_length=100,
                                 verbose_name=_('sub_title'))
    left_title = models.CharField(max_length=100,
                                  verbose_name=_('left_title'))
    left_description = models.TextField(verbose_name=_('left_description'))
    right_title = models.CharField(max_length=100,
                                   verbose_name=_('right_title'))
    right_description = models.TextField(verbose_name=_('right_description'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('about')
        verbose_name_plural = _('about')


class TestimonialImageModel(models.Model):
    image = models.ImageField(upload_to='testimonial_image',
                              verbose_name=_('image'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('testimonial image')
        verbose_name_plural = _('testimonial images')


class ClientModel(models.Model):
    image = models.ImageField(upload_to='client_image',
                              verbose_name=_('image'))
    name = models.CharField(max_length=100, verbose_name=_('name'))
    profession = models.CharField(max_length=100,
                                  verbose_name=_('profession'))
    description = models.TextField(verbose_name=_('description'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')
