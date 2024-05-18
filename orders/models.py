from django.db import models

from products.models import Product


class Order(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField(default=0.00)

    def __str__(self):
        return self.product.title

# Create your models here.
