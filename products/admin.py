from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from products.models import ProductCategoryModel, ProductModel


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


@admin.register(ProductCategoryModel)
class ProductModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ProductModel)
class ProductModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'category', 'price', 'created_at']
    list_filter = ['title', 'category', 'price', 'created_at']
    search_fields = ['title', 'category']
