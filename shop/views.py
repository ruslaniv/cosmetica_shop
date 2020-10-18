from django.views.generic import ListView, DetailView, TemplateView
from .models import Product


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
    print(self.kwargs)
    category_slug = self.kwargs['category_slug']
    print(category_slug, 'category')
    products = Product.objects.filter(category__slug__icontains=category_slug)
    print(products)
    return products


class BrandView(ListView):
  model = Product
  template_name = 'shop/list.html'
  context_object_name = 'all_products'

  def get_queryset(self, **kwargs):
    print(self.kwargs)
    brand_slug = self.kwargs['brand_slug']
    print(brand_slug, 'brand')
    # products = Product.objects.filter(brand__slug__icontains=brand_slug)
    products2 = Product.objects.all()
    print(products2)
    return products2


class ProductDetail(DetailView):
  model = Product
  template_name = 'shop/detail.html'
