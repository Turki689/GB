from django.db import models
from django.utils.translation import gettext_lazy as _

from categories.models import Category


class Product(models.Model):
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_img_upload_path(instance, filename):
        return f'{instance.title}/images/{filename}'
    title = models.CharField(max_length=255)
    unit_price = models.FloatField(default=0.00)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company_logo = models.ImageField(upload_to=get_img_upload_path)


    def __str__(self):
        return self.title
