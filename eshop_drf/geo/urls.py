from django.urls import path, include
from rest_framework import routers
from .views import CountryView, StateView, DistrictView

router = routers.DefaultRouter()
router.register('county', CountryView)
router.register('state', StateView)
router.register('district', DistrictView)

urlpatterns = [
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls'))
]