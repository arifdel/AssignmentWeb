from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

from .models import Category
from .models import Subcategory
from .models import Product
from .serializer import CategorySerializer
from .serializer import SubcategorySerializer
from .serializer import ProductSerializer

@api_view(('GET',))
def index(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
        
 
@api_view(('GET',))
def index_products(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
 
@api_view(['POST', 'GET',])
def add_category(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  


@api_view(['POST', 'GET',])
def add_product(request):
    if request.method == 'POST':
        print ('Check point1')
        print (request.data)
        category_name = request.GET['name']
        print (category_name)
        subcategory_name = request.GET['subcat']
        print (subcategory_name)
        category = Category.objects.all().filter(name = category_name)
        sub_category = Subcategory.objects.all().filter(subcat = subcategory_name)
        print (sub_category)
        print (request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            print ('hello')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




