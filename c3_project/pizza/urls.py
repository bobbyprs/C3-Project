from django.urls import path,include
from .views import PizzaViewset,ToppingsViewset,TypeToppingsViewset
from django.conf.urls import url
from django.conf import settings
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('pizza' , PizzaViewset , basename = 'pizza')
router.register('toppings',ToppingsViewset,basename='Veg')
router.register('types',TypeToppingsViewset,basename='NonVeg')

urlpatterns = [
    path('pizza/' , include(router.urls))
]