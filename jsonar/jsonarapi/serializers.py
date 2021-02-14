from rest_framework import serializers
from . models import Customers,Payment,Rentals,Films,Actors

class Customersserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Customers
        fields=('id','Address','City','Country','District','Firstname','Lastname','Phone')

class Paymentserializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'

class Rentalsserializer(serializers.ModelSerializer):
    class Meta:
        model=Rentals
        fields='__all__'

class Actorsserializer(serializers.ModelSerializer):
    class Meta:
        model=Actors
        fields='__all__'

class Filmsserializer(serializers.ModelSerializer):
    actors = Actorsserializer(many=True, read_only=True)
    class Meta:
        model=Films
        fields=['actors','Title']
