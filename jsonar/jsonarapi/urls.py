from . import views
from django.urls import path
from .models import Customers
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'films', views.FilmsViewSet)
router.register(r'actors', views.ActorsViewSet)
router.register(r'rentals', views.RentalsViewSet)


urlpatterns=[
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]