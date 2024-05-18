from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from categories.models import Category

admin.site.register(Category, MPTTModelAdmin)
