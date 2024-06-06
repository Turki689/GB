from django.urls import path

from companies.views import CompanyDetailAPIView,CompanyListAPIView

app_name = 'products'
urlpatterns = [
    path('', CompanyListAPIView.as_view(), name='index'),
    path('<str:company_slug>/', CompanyDetailAPIView.as_view(), name='details'),

]
