from django.urls import path
from django.urls.conf import include

from django.urls import path
from .views import ProductList

urlpatterns = [
    path('valerdat/products/', ProductList.as_view(), name='product-list'),
]
