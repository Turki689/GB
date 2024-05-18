from django.db import models



# Create your models here.


class Company (models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField()
    def __str__(self):
        return self


# class SubCategory(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True)
#     category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name



