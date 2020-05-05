from django import forms
from django.forms import ModelForm
from .models import Toppings, Pizza, OrderPizza

SIZE =[
    ("s", "small"),
    ("l", "large")
]

class PizzaFrom(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = [
            'name',
            'type',
            'price_small',
            'price_large',
            'number_toppings',
            'toppings'
        ]

class ToppingsForm(forms.ModelForm):
    class Meta:
        model = Toppings
        fields = [
            'name'
        ]

class OrderPizzaForm(forms.ModelForm):


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # self.fields['toppings'].widget.attrs.update({'class': 'selectpicker dropdown-menu-right',
        #                                              'title': "Toppings",
        #                                              "data-live-search": "true",
        #                                              "data-max-options": 1})


    class Meta:
        model = OrderPizza
        fields = [
            'pizza',
        ]
