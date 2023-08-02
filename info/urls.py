from django.urls import path

from info.views import AboutTemplateView, TestimonialCreateView

app_name = 'info'

urlpatterns = [
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('testimonials/', TestimonialCreateView.as_view(),
         name='testimonials'),
]
