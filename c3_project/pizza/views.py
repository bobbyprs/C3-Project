from django.shortcuts import render
from .serializers import PizzaSerializers,ToppingsSerializers,TypeToopingSerializers
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from .models import Pizza,Toopings,TypeToopings
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


'''
Hear iam using modelViewset because this are time saving and effective all Though people say it is a bit confusing 
it saves  lot time  and speed up work as well
'''

class ToppingsViewset(viewsets.ModelViewSet):
    queryset =Toopings.objects.all()
    serializer_class=ToppingsSerializers

class TypeToppingsViewset(viewsets.ModelViewSet):
    queryset =TypeToopings.objects.all()
    serializer_class=TypeToopingSerializers

class PizzaViewset(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializers 
    filter_backends = (DjangoFilterBackend,) #For Filtering according to the specific model fields
    filter_fields = ('type','size')