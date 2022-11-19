from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.filters import ProductFilter
from apps.models import Category, ProductImages, Product
from apps.serializer import CategoryModelSerializer, ProductImagesModelSerializer, ProductModelSerializer


# Create your views here.

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'


class ProductImageGenericAPIView(GenericAPIView):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImagesModelSerializer
    parser_classes = (MultiPartParser, )
    lookup_url_kwarg = 'id'

    def get(self, request):
        image = ProductImages.objects.all()
        serializer = self.serializer_class(image, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    lookup_url_kwarg = 'id'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = ProductFilter
    search_field = ['id', 'name']
    filterset_fields = {
        'price': ['gte', 'lte']
    }
