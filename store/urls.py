from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path('products/', views.product_list, name='index'),
    path('products/<int:pk>',views.product_detail),
    path('search/', views.search, name='search'),
    # path('products/subcategory/<slug:subcategory_slug>/', views.list_by_subcategory, name='product_list_by_subcategory'),
    path('products/category/<slug:category_slug>/',views.list_by_category , name='product_list_by_category'),
]
