from django.contrib import admin
from django.contrib.admin import ModelAdmin
from companies.models import  Company


admin.site.register(Company, ModelAdmin)