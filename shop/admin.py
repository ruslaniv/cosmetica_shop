from django.contrib import admin
from .models import Category, Product, Brand


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['category_name', 'slug']
  prepopulated_fields = {'slug': ('category_name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
  list_display = ['brand_name', 'slug']
  prepopulated_fields = {'slug': ('brand_name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['product_name', 'brand', 'slug', 'price', 'available', 'created', 'updated']
  list_filter = ['available', 'created', 'updated']
  list_editable = ['price', 'available']
  prepopulated_fields = {'slug': ('product_name',)}
