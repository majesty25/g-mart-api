from rest_framework import generics
from rest_framwork import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framwork.permisions import IsAuthenticated
from models import Product
from serializers import ProductSerializer, ProductDetailSerializer

# class ProductListCreateView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerialize


class ProductViewSet(viewsets.ModuleViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
