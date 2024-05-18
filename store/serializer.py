from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets



# Create your views here.



class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    slug = serializers.SlugField()

class SubCategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    category = CategorySerializer()
    slug = serializers.SlugField()

class CompanySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugField()
    description = serializers.CharField(max_length=255)