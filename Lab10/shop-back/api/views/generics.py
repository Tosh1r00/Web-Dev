from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Product, Category
from api.serialiers import ProductSerializer, CategorySerializer

#GET + POST for productList
class ListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#GET + PUT + DELELET for product/:id
class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        lookup_url_kwarg = 'product_id'

#GET + POST for categoryList
class CategoryListAPIView(generics.ListCreateAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer

#GET + PUT + DELELET for category/:id
class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
        lookup_url_kwarg = 'category_id'


# Custom endpoint to return list of products by a category
class CategoryProductsAPIView(APIView):
    def get(self, request, category_id):
        try:
         category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        
        products = category.products.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)