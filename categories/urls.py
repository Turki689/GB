from django.urls import path, include

from categories.views import CategoryListAPIView

app_name = 'categories'

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name='index'),
    path('<str:slug>/products/',include('products.urls',namespace='products'))
]
