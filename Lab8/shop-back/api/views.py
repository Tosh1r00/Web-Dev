from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category,Product
from .serialiers import CategorySerializer, ProductSerializer

class CategoryViewSet (viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#Custom decorator
    @action(detail=True,methods=['get'])
    def products(self,request,pk = None):
        categ = self.get_object() # по pk находим категорию
        products = Product.objects.filter(category = categ) # фильтруем products по категории
        serializer = ProductSerializer(products, many = True) #  сериализатор для списка продуктов.
        return Response (serializer.data) # готовый JSON; Response - DRF способ возвращает вывод


class ProductViewSet (viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CategorySerializer