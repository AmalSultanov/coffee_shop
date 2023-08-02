from django.db import models
from django.utils.translation import gettext_lazy as _


class HomeBannerModel(models.Model):
    image = models.ImageField(upload_to='home_banners',
                              verbose_name=_('image'))
    upper_title = models.CharField(max_length=100,
                                   verbose_name=_('upper_title'))
    middle_title = models.CharField(max_length=100,
                                    verbose_name=_('middle_title'))
    lower_title = models.CharField(max_length=100,
                                   verbose_name=_('lower_title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return f"{self.upper_title} {self.middle_title} {self.lower_title}"

    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banners')


class ReservationInfoModel(models.Model):
    discount_title = models.CharField(max_length=100,
                                      verbose_name=_('discount_title'))
    sub_title = models.CharField(max_length=100, verbose_name=_('sub_title'))
    description = models.TextField(verbose_name=_('description'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.discount_title

    class Meta:
        verbose_name = _('reservation info')
        verbose_name_plural = _('reservation info')


class ReservationModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    date = models.DateField(verbose_name=_('date'))
    time = models.TimeField(verbose_name=_('time'))
    number_of_people = models.IntegerField(verbose_name=_('number_of_people'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('reservation')
        verbose_name_plural = _('reservations')


class ContactInfoModel(models.Model):
    address = models.CharField(max_length=100, verbose_name=_('address'))
    phone = models.CharField(max_length=50, verbose_name=_('phone'))
    email = models.EmailField(verbose_name=_('email'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = _('contact info')
        verbose_name_plural = _('contact info')


class ContactModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    subject = models.CharField(max_length=100, verbose_name=_('subject'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
