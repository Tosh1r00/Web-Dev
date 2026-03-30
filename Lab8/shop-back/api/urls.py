from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('categories',views.CategoryViewSet) # «для адреса `/categories/` используй `CategoryViewSet`»
router.register('products', views.ProductViewSet)

urlpatterns = router.urls #роутер сам генерирует все нужные URL


