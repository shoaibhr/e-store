from django.shortcuts import render
from .models import Product
from .serializers import CategorySerializer,ProductSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
# Create your views here.

class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('id')

class ProductDetail(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()