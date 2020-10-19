from django.views.generic import ListView, DetailView, TemplateView
from .models import Product
import _logger


class HomeView(TemplateView):
  template_name = 'shop/home.html'


class ProductListView(ListView):
  model = Product
  template_name = 'shop/list.html'
  context_object_name = 'all_products'


class CategoryView(ListView):
  model = Product
  template_name = 'shop/list.html'
  context_object_name = 'all_products'

  def get_queryset(self, **kwargs):
    _logger.logger.debug(self.kwargs)
    category_slug = self.kwargs['category_slug']
    _logger.logger.debug(category_slug)
    products = Product.objects.filter(category__slug__icontains=category_slug)
    _logger.logger.debug(products)
    return products


class BrandView(ListView):
  model = Product
  template_name = 'shop/list.html'
  context_object_name = 'all_products'

  def get_queryset(self, **kwargs):
    _logger.logger.debug(self.kwargs)
    brand_slug = self.kwargs['brand_slug']
    _logger.logger.debug(brand_slug)
    products = Product.objects.filter(brand__slug__icontains=brand_slug)
    _logger.logger.debug(products)
    return products


class ProductDetail(DetailView):
  model = Product
  template_name = 'shop/detail.html'
