from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView

from products.models import ProductModel


def load_more_hot_data(request):
    try:
        offset = int(request.GET['offset'])
    except KeyError:
        offset = 0

    limit = int(request.GET['limit'])
    hot_products = ProductModel.objects.filter(
        category__title_en__contains='hot')[offset:offset + limit]
    product_data = [
        {
            'image': product.image.url,
            'title': product.title,
            'category': product.category.title,
            'price': product.price,
            'description': product.description
        } for product in hot_products]
    t = render_to_string('menu_hot_item.html', {'hot_products': product_data})

    return JsonResponse({'hot_products': t})


def load_more_cold_data(request):
    try:
        offset = int(request.GET['offset'])
    except KeyError:
        offset = 0

    limit = int(request.GET['limit'])
    cold_products = ProductModel.objects.filter(
        category__title_en__contains='cold')[offset:offset + limit]
    product_data = [
        {
            'image': product.image.url,
            'title': product.title,
            'category': product.category.title,
            'price': product.price,
            'description': product.description
        } for product in cold_products]
    t = render_to_string('menu_cold_item.html',
                         {'cold_products': product_data})

    return JsonResponse({'cold_products': t})


class MenuListView(ListView):
    template_name = 'menu.html'

    def get_queryset(self):
        qs = ProductModel.objects.all()

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hot_products'] = ProductModel.objects.filter(
            category__title_en__contains='hot')[:2]
        context['cold_products'] = ProductModel.objects.filter(
            category__title_en__contains='cold')[:2]
        context['total_hot_products'] = ProductModel.objects.filter(
            category__title_en__contains='hot').count()
        context['total_cold_products'] = ProductModel.objects.filter(
            category__title_en__contains='cold').count()

        return context
