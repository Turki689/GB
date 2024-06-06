import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from categories.models import Category
from products.models import Product


class Company(models.Model):
    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    website = models.TextField(max_length=255)
    phone = models.CharField(max_length=14, blank=True)
    address = models.TextField()
    email = models.EmailField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

# Create your models here.
