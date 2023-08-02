from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductCategoryModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('product category')
        verbose_name_plural = _('product categories')


class ProductModel(models.Model):
    image = models.ImageField(upload_to='product_image',
                              verbose_name=_('image'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    category = models.ForeignKey(ProductCategoryModel,
                                 on_delete=models.PROTECT,
                                 related_name='products',
                                 verbose_name=_('category'),
                                 blank=True,
                                 null=True)
    price = models.CharField(max_length=10, verbose_name=_('price'))
    description = models.TextField(verbose_name=_('description'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
