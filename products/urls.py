from django.urls import path

from products.views import (load_more_hot_data, load_more_cold_data,
                            MenuListView)

app_name = 'products'

urlpatterns = [
    path('load1/', load_more_hot_data, name='load1'),
    path('load2/', load_more_cold_data, name='load2'),
    path('', MenuListView.as_view(), name='menu'),
]
