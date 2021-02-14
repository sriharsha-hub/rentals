from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Customers,Films,Actors,Rentals
from .serializers import Customersserializer,Filmsserializer,Actorsserializer,Rentalsserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all().order_by('id')
    serializer_class = Customersserializer
    filter_fields = {'some_field': ['startswith']}

class FilmsViewSet(viewsets.ModelViewSet):
    queryset = Films.objects.all().order_by('Title')
    serializer_class = Filmsserializer

class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actors.objects.all().order_by('actorId')
    serializer_class = Actorsserializer

class RentalsViewSet(viewsets.ModelViewSet):
    queryset = Rentals.objects.all().order_by('rentalId')
    serializer_class = Rentalsserializer
    filter_fields = {'CustomerId': ['startswith']}








