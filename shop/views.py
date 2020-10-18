from django.views.generic import ListView, DetailView, TemplateView
from .models import Product


class HomeView(TemplateView):
  template_name = 'shop/home.html'
