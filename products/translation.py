from modeltranslation.translator import register, TranslationOptions

from products.models import ProductCategoryModel, ProductModel


@register(ProductCategoryModel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ProductModel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
