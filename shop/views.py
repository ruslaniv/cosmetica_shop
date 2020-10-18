from django.views.generic import ListView, DetailView, TemplateView
from .models import Product


class HomeView(TemplateView):
  template_name = 'shop/home.html'


class ProductListView(ListView):
  model = Product
  template_name = 'shop/list.html'
  context_object_name = 'all_products'
