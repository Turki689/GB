from django.contrib import admin
from django.contrib.admin import ModelAdmin

from products.models import Product

admin.site.register(Product, ModelAdmin)
