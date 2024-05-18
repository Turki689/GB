from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('store/', include("store.urls"))
    path('categories/', include("categories.urls", namespace="categories")),
    path('products/', include('products.urls', namespace='products')),
    path('orders/', include('orders.urls', namespace='orders'))
]
