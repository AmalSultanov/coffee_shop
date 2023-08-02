from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from info.models import AboutModel, TestimonialImageModel, \
    ClientModel


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


@admin.register(AboutModel)
class AboutModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(TestimonialImageModel)
class TestimonialImageModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ClientModel)
class ClientModelAdmin(MyTranslationAdmin):
    list_display = ['name', 'profession', 'created_at']
    list_filter = ['profession', 'created_at']
    search_fields = ['profession', 'title']
