from django.db import models
from multiselectfield import MultiSelectField
from django.utils.translation import ugettext_lazy as _

# Create your models here.
"""
so their can be different kind of toppings for example so i did this in a superate model 
i think this might be the proper way to do because later insted of editing the code u can 
dynamically add from the front end so 

"""

class TypeToopings(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    
    def __str__(self):
        return self.name

'''
This model write hear is for the adding the toppings and the forign key field is for seperating the 
different kinds of toppings 
'''

class Toopings(models.Model):
    name = models.CharField(max_length=60)
    toopings =models.ForeignKey(TypeToopings,on_delete=models.CASCADE,blank=False,null=False)

    def __str__(self):
        return self.name

        
'''
for adding the pizza
'''

class Pizza(models.Model):

    class Types(models.TextChoices):
        REGULAR = "Regular ","REGULAR"
        SQUARE = "Square","SQUARE"

    default_type = Types.REGULAR

    type = models.CharField(choices=Types.choices, default=[], null=False, blank=False,max_length=255 ) 

    class Size(models.TextChoices):
        REGULAR = "Regular","REGULAR"
        MEDIUM = "Medium","MEDIUM"
        LARGE = "Large" , "LARGE"
        EXTRA_LARGE = "Extra_Large","EXTRA_LARGE"

    default_type = Size.REGULAR

    size = models.CharField(choices=Size.choices, default=[], null=False, blank=False,max_length=255 )

    toppings = models.ManyToManyField(Toopings)

    

    def __str__(self):
        return self.type