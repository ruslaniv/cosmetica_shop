from django.db import models


class Category(models.Model):
  category_name = models.CharField(max_length=128, db_index=True)
  slug = models.SlugField(max_length=128, unique=True)

  class Meta:
    ordering = ('category_name',)
    verbose_name = 'category'
    verbose_name_plural = 'categories'

  def __str__(self):
    return self.category_name


class Brand(models.Model):
  brand_name = models.CharField(max_length=128, db_index=True)
  slug = models.SlugField(max_length=128, unique=True)

  class Meta:
    ordering = ('brand_name',)
    verbose_name = 'brand'
    verbose_name_plural = 'brands'

  def __str__(self):
    return self.brand_name


class Product(models.Model):
  category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
  brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
  product_name = models.CharField(max_length=256, db_index=True)
  slug = models.SlugField(max_length=256, db_index=True)
  image = models.ImageField(upload_to='assets/productimages/%Y/%m/%d', blank=True)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  available = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ('product_name',)
    index_together = (('id', 'slug'),)

  def __str__(self):
    return self.product_name
