from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from apps.models import Category, ProductImages, Product


class CategoryModelSerializer(ModelSerializer):
    def validate(self, attrs):
        if Category.objects.filter(name=attrs['name']).exists():
            raise ValidationError('this name is exist')
        return attrs

    class Meta:
        model = Category
        exclude = ('slug', )


class ProductImagesModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['images'] = ProductImagesModelSerializer(instance.product_images.first()).data
        represent['category'] = CategoryModelSerializer(instance.category).data
        return represent

    class Meta:
        model = Product
        fields = '__all__'
