from rest_framework.generics import ListAPIView

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryListAPIView(ListAPIView):
    model = Category
    serializer_class = CategorySerializer
    filterset_fields = {
        'slug': ['in'],
        "parent__slug": ['exact']
    }
    search_fields = ['name', 'slug', 'parent__name', 'parent__slug', 'id']
    ordering_fields = ['name', 'id']

    def get_queryset(self):
        return Category.objects.all()
