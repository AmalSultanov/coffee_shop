from modeltranslation.translator import register, TranslationOptions

from info.models import AboutModel, TestimonialImageModel, ClientModel


@register(AboutModel)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'left_title', 'left_description',
              'right_title', 'right_description',)


@register(TestimonialImageModel)
class TestimonialImageTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ClientModel)
class ClientTranslationOptions(TranslationOptions):
    fields = ('name', 'profession', 'description',)
