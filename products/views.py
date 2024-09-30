from django.shortcuts import render
from .models import Product
from .serializers import CategorySerializer,ProductSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
# Create your views here.

class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    #queryset = Product.objects.all().order_by('id') #all products irrespective of category
    
    #filter based on category
    # def get_queryset(self):
    #     category_id = self.request.query_params.get('category', None)
        
    #     if category_id is not None:
    #         return Product.objects.filter(category_id=category_id).order_by('id')
    #     return Product.objects.all().order_by('id')
        
    #filter based on multiple filters
    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.query_params.get('category', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        available = self.request.query_params.get('available', None)
        
        if category_id:
            queryset = Product.objects.filter(category_id=category_id)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if available is not None:  # Since it's a boolean, explicitly check for None
            queryset = queryset.filter(available=available.lower() == 'true')
            
        return queryset.order_by('id')
    
    
class ProductDetail(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()