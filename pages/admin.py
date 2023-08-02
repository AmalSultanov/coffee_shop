from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from pages.models import HomeBannerModel, ContactInfoModel, ContactModel, \
    ReservationInfoModel, ReservationModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(HomeBannerModel)
class HomeBannerModelAdmin(MyTranslationAdmin):
    list_display = ['upper_title', 'middle_title', 'lower_title', 'created_at']
    list_filter = ['created_at']


@admin.register(ReservationInfoModel)
class ReservationInfoModelAdmin(MyTranslationAdmin):
    list_display = ['discount_title', 'sub_title', 'description', 'created_at']
    list_filter = ['discount_title', 'created_at']
    search_fields = ['discount_title']


@admin.register(ReservationModel)
class ReservationModelAdmin(MyTranslationAdmin):
    list_display = ['name', 'date', 'time', 'number_of_people', 'created_at']
    list_filter = ['date', 'time', 'number_of_people', 'created_at']
    search_fields = ['name', 'date', 'time', 'number_of_people']


@admin.register(ContactInfoModel)
class ContactInfoModelAdmin(MyTranslationAdmin):
    list_display = ['address', 'phone', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['address', 'phone', 'email']


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    list_filter = ['subject', 'created_at']
    search_fields = ['subject']
