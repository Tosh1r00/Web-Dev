from rest_framework import generics, mixins
from api.models import Product
from api.serialiers import ProductSerializer


#4.1) Level 4 — Mixins + GenericAPIView
class ProductListApiView (mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    #два след fields - обзательно к написанию, они используются внутри библиотеки mixins
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    

class ProductDetalilApiView ( mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin, 
                              mixins.DestroyModelMixin,
                              generics.GenericAPIView):
    
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        lookup_url_kwarg = 'product_id' #ищет продукт по айдишке из url

        def get(self,request,product_id):
             return self.retrieve(request,product_id)
        def put(self, request, product_id):
            return self.update(request, product_id)
        def delete(self, request, product_id):
            return self.destroy(request, product_id)