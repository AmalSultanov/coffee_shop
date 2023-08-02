from modeltranslation.translator import register, TranslationOptions

from pages.models import HomeBannerModel, ReservationInfoModel, \
    ReservationModel, ContactInfoModel


@register(HomeBannerModel)
class HomeBannerTranslationOptions(TranslationOptions):
    fields = ('upper_title', 'middle_title', 'lower_title',)


@register(ReservationInfoModel)
class ReservationInfoTranslationOptions(TranslationOptions):
    fields = ('discount_title', 'sub_title', 'description',)


@register(ReservationModel)
class ReservationTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(ContactInfoModel)
class ContactInfoTranslationOptions(TranslationOptions):
    fields = ('address',)
