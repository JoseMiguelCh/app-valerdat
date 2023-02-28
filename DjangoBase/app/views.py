from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductList(generics.ListCreateAPIView):
    """This class defines the create behavior of products endpoint in rest api."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer