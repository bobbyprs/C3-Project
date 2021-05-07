from rest_framework import serializers
from .models import Pizza , Toopings,TypeToopings


class ToppingsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Toopings
        fields = ('id','name','toopings')

class TypeToopingSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = TypeToopings
        fields = ('id','name')

class PizzaSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Pizza
        fields =('id','url','type','size','toppings')

    