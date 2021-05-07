from django import forms
from django.db import transaction
from .models import Pizza


class PizzaForm(forms.ModelForm):
    class Meta:
        models = Pizza
        fields = ['type','size','toppings']