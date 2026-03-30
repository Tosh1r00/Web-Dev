from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer): #превращем категорию в JSON - response
    class Meta: 
        model = Category # работаем с этой моделью
        fields = '__all__' # берем все филды

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'