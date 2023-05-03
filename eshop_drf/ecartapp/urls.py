from django.urls import path, include
from rest_framework import routers
from .views import CategoryView, BrandView, ProductView, UserView, AddressView, CartView

router = routers.DefaultRouter()
router.register('categories', CategoryView)
router.register('brands', BrandView)
router.register('products', ProductView)
router.register('users', UserView)
router.register('address', AddressView)
router.register('cart', CartView)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]





