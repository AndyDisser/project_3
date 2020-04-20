from django.db import models

SIZE_PIZZA_CHOICES = [
    ("sm", "small"),
    ("lg", "large")
]

TYPE_CHOICES = [
    ("reg", "Regular Pizza"),
    ("sic", "Sicilian Pizza")
]
# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64, choices=TYPE_CHOICES, blank=False)
    price_small = models.DecimalField(max_digits=8, decimal_places=2)
    price_large = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"name: {self.name}, type: {self.type}, small: {self.price_small}, large: {self.price_large}"

class Toppings(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Subs(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    price_large = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.name}"

class Addition(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Dinner_Platters(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.DecimalField(max_digits=8, decimal_places=2)
    price_large = models.DecimalField(max_digits=8, decimal_places=2)

class Cart(models.Model):
    user = pass
    pizzas = models.ManyToManyField(Pizza, blank=True)
    toppings = models.ManyToManyField(Toppings, blank=True)
    subs = models.ManyToManyField(Subs, blank=True)
    additions = models.ManyToManyField(Additions, blank=True)
    pastas = models.ManyToManyField(Pasta, blank=True)
    salads = models.ManyToManyField(Salad, blank=True)
    dinner_platters = models.ManyToManyField(Dinner_Platters, blank=True)
