from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from info.models import AboutModel, ClientModel
from pages.forms import ReservationModelForm, ContactModelForm
from pages.models import (HomeBannerModel, ContactInfoModel,
                          ReservationInfoModel)
from products.models import ProductModel


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = HomeBannerModel.objects.all()
        context['info'] = AboutModel.objects.all()
        context['hot_products'] = ProductModel.objects.filter(
            category__title_en__contains='hot')[:3]
        context['cold_products'] = ProductModel.objects.filter(
            category__title_en__contains='cold')[:3]
        context['clients'] = ClientModel.objects.all()[:6]

        return context


class ServiceTemplateView(TemplateView):
    template_name = 'service.html'


class ReservationCreateView(SuccessMessageMixin, CreateView):
    template_name = 'reservation.html'
    form_class = ReservationModelForm
    success_message = 'You have successfully booked a table!'

    def get_success_url(self):
        return reverse('pages:reservation')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservation_info'] = ReservationInfoModel.objects.all()

        return context


class ContactCreateView(SuccessMessageMixin, CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm
    success_message = 'Your message was sent successfully!'

    def get_success_url(self):
        return reverse('pages:contact')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = ContactInfoModel.objects.all()

        return context
