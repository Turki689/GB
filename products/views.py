from rest_framework.generics import ListAPIView, get_object_or_404, RetrieveAPIView

from categories.models import Category
from products.models import Product
from products.serializers import ProductSerializer


class ProductsListAPIView(ListAPIView):
    model = Product
    serializer_class = ProductSerializer
    filterset_fields = {
        "category__slug": ['exact']
    }
    search_fields = ['title', 'description', 'category__name', 'category__slug', 'category__id', 'id']
    ordering_fields = ['unit_price', 'title', 'date']

    def get_queryset(self):
        if slug := self.kwargs.get('slug', None):
            category = get_object_or_404(Category, slug=slug)
            return Product.objects.filter(
                category_id__in=category.get_descendants(include_self=True).values_list('id', flat=True)
            )
        return Product.objects.all()


class ProductDetailAPIView(RetrieveAPIView):
    model = Product
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'product_slug'

    def get_queryset(self):
        if slug := self.kwargs.get('slug', None):
            category = get_object_or_404(Category, slug=slug)
            return Product.objects.filter(
                category_id__in=category.get_descendants(include_self=True).values_list('id', flat=True)
            )
        return Product.objects.all()
