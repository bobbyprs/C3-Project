from django.contrib import admin
from .models import Pizza,Toopings,TypeToopings
from .forms import PizzaForm 
# Register your models here.


class PizzaAdmin(admin.ModelAdmin):

    add_form = PizzaForm
    list_display =('type','size')
    list_filter=('type','size')    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'type','size','toppings')}
        ),
    )    


admin.site.register(Pizza ,PizzaAdmin)
admin.site.register( Toopings)
admin.site.register( TypeToopings)
