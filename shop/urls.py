from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
  path('', views.HomeView.as_view(), name='homepage'),
  path('listall', views.ProductListView.as_view(), name='all_product_list'),
  path('brand/<slug:brand_slug>', views.BrandView.as_view(), name='product_list_by_brand'),
  path('category/<slug:category_slug>', views.CategoryView.as_view(), name='product_list_by_category'),
  path('<slug:product_category_slug>/<slug:product_brand_slug>/<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
]
