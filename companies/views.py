from django.views.generic import ListView
from rest_framework.generics import ListAPIView,get_object_or_404,RetrieveAPIView
from categories.models import Category
from companies.models import Company
from companies.serializers import CompanySerializer



class CompanyListAPIView(ListAPIView):
    model = Company
    serializer_class = CompanySerializer
    filterset_fields = {
            "category__slug": ['exact']
        }
    search_fields = ['name', 'description', 'category__name', 'category__slug', 'category__id'
                         ]
    ordering_fields = ['name', 'category__name',]


    def get_queryset(self):
      if slug := self.kwargs.get('slug', None):
        category = get_object_or_404(Company, slug=slug)
        return Company.objects.filter(
            category_id__in=category.get_descendants(include_self=True).values_list('id', flat=True),
        )
      return Company.objects.all()

class CompanyDetailAPIView(RetrieveAPIView):
    model = Company
    serializer_class = CompanySerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'company_slug'

    def get_queryset(self):
        if slug := self.kwargs.get('slug', None):
            category = get_object_or_404(Category, slug=slug)
            return Company.objects.filter(
                category_id__in=category.get_descendants(include_self=True).values_list('id', flat=True)
            )
        return Company.objects.all()

# Create your views here.
