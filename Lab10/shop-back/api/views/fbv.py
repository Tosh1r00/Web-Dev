from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Product
from api.serialiers import ProductSerializer

# 2.1)product-list 
@api_view(['GET','POST']) #лучше безопасность реквестов, все не перечисленные реквесты улетают в 405(Ошибка)
def product_list(request):
    if request.method() == 'GET':
        products = Product.objects.all() #берем все продукты из базы данных
        serializer = ProductSerializer(products, many = True) #Json - parse

        return Response(serializer.data) #В ответе возвращаем Json обьект


    elif request.method() == 'POST':
        serializer = ProductSerializer( data = request.data )
        if serializer.is_valid():
            serializer.save() #если данные правильные, то создается новый обьект в сериалайзер
            return Response ( serializer.data , status = status.HTTP_201_CREATED )
        
        return Response ( serializer.errors , status = status.HTTP_400_BAD_REQUEST )
    
# 2.2)product-detail
@api_view(['GET','PUT','DELETE'])
def product_detail(request, product_id = None):

    #проверка на наличие продукта в листе
    try:   
        product = Product.objects.get(pk = product_id)
    except Product.DoesNotExist as e:
        return Response ({'Error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
    #методы
    if request.method == 'GET':
        serializer = ProductSerializer(product) # Json-parse
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(instance = product, data = request.data) #instance = какой продукт обновляем, и за ним новые данные

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #всегда возвращаем ошибку если не_валид
    
    elif request.method() == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



