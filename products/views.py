from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import ProductSerializer, CategorySerializer

class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer