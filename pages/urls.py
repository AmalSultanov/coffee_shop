from django.urls import path

from pages.views import (ContactCreateView, ReservationCreateView,
                         ServiceTemplateView, HomeTemplateView)

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('reservation/', ReservationCreateView.as_view(),
         name='reservation'),
    path('service/', ServiceTemplateView.as_view(), name='service'),
    path('', HomeTemplateView.as_view(), name='home'),
]
