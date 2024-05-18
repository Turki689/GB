from django.urls import path

from orders.views import OrderCreateAPIView
app_name = 'orders'
urlpatterns = [
    path('add/', OrderCreateAPIView.as_view(), name="add")
]
