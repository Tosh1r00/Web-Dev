from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Product
from api.serialiers import ProductSerializer

#3.1) Class - ProductList
class ProductListApiView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#3.1) Class - ProductDetail
class ProductDetailApiView:
    def get_object(self,product_id):

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist as e:
            return Response ( {'Error':str(e)}, status=status.HTTP_404_NOT_FOUND )
        
    def get(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    


    def put(self,request,product_id):
        product = self.get_object(product_id) 
        serializer = ProductSerializer(instance = product, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,product_id):
        product = self.get_object(product_id)
        product.delete()
        return Response( status=status.HTTP_204_NO_CONTENT )