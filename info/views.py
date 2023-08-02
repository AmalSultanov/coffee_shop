from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from info.forms import ClientModelForm
from info.models import AboutModel, ClientModel


class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = AboutModel.objects.all()

        return context


class TestimonialCreateView(CreateView):
    template_name = 'testimonial.html'
    form_class = ClientModelForm

    def get_success_url(self):
        return reverse('info:testimonials')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = ClientModel.objects.all()

        return context
