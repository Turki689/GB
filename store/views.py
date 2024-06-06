from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.urls import include,path
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Company
from products.models import Product
from ..categories.models import Category
from .serializer import ProductSerializer,CategorySerializer,SubCategorySerializer,CompanySerializer
from django.db.models import Q


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()

    sort = request.GET.get('sort_by', None)
    if sort:
        if sort == 'date':
            products = products.order_by('-created_at')
        elif sort == 'unit_price_A':
            products = products.order_by('unit_price')
        elif sort == 'unit_price_D':
            products = products.order_by('-unit_price')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view()
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(subcategory__category=category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def list_by_subcategory(request, subcategory_slug):
#     subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
#     products = Product.objects.filter(subcategory=subcategory)
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


@api_view(['GET'])
def search(request):
    query = request.GET.get('q', '')

    products = Product.objects.filter(Q(title__icontains=query) | Q(company__name__icontains=query))
    company = Company.objects.filter(name__icontains=query)

    product_serializer = ProductSerializer(products, many=True)
    company_serializer = CompanySerializer(Company, many=True)

    results = {
        'products': product_serializer.data,
        'companies': company_serializer.data
    }

    return Response(results)



