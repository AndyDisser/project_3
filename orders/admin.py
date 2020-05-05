from django.contrib import admin

from .models import Pizza, Toppings, Subs, Addition, Pasta, Salad, Dinner_Platters, OrderPizza, OrderSub, OrderPasta, OrderSalad, OrderPlatter, Checkouts

# Register your models here.

admin.site.register(Pizza)
admin.site.register(Dinner_Platters)
admin.site.register(Salad)
admin.site.register(Pasta)
admin.site.register(Addition)
admin.site.register(Subs)
admin.site.register(Toppings)
admin.site.register(OrderPizza)
admin.site.register(OrderSub)
admin.site.register(OrderPasta)
admin.site.register(OrderSalad)
admin.site.register(OrderPlatter)
admin.site.register(Checkouts)
