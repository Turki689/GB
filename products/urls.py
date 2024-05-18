from django.urls import path

from products.views import ProductsListAPIView, ProductDetailAPIView

app_name = 'products'
urlpatterns = [
    path('', ProductsListAPIView.as_view(), name='index'),
    path('<str:product_slug>/', ProductDetailAPIView.as_view(), name='details'),

]
