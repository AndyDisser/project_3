from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

SIZE_PIZZA_CHOICES = [
    ("sm", "small"),
    ("lg", "large")
]

TYPE_CHOICES = [
    ("reg", "Regular Pizza"),
    ("sic", "Sicilian Pizza")
]
# Create your models here.
class Toppings(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
            return f"{self.name}"

class Pizza(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64, choices=TYPE_CHOICES, blank=False)
    price_small = models.DecimalField(max_digits=8, decimal_places=2)
    price_large = models.DecimalField(max_digits=8, decimal_places=2)
    number_toppings = models.PositiveIntegerField(blank=True)
    toppings = models.ManyToManyField(Toppings, blank=True, related_name="topping")

    class Meta:
        ordering = ['type']

    def __str__(self):
        return f"{self.name}"

class Addition(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Subs(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    price_large = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    additions = models.ManyToManyField(Addition, blank=True)

    def __str__(self):
        return f"{self.name}"


class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name}"


class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name}"

class Dinner_Platters(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.DecimalField(max_digits=8, decimal_places=2)
    price_large = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name}"


# create a order-group that contains the cart of a person when
# Collecting all under one id. It also takes the time when the order
# is collected which is the foundation for displaying the orders for
# the owner of the pizzeria and to show the customers their past orders.

# One OrderPizza,... has to have only one order-group, but one order-group
# has to be able to contain multiple orders.
# --> one to many relationship

class Checkouts(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_checkouts")
    # could add DateTimeField(auto_add) to show the user when the pizza was delivered

class OrderPizza(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders_pizza')
    pizza = models.ManyToManyField(Pizza, blank=True)
    toppings = models.ManyToManyField(Toppings, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False) # already in Checkouts, so maybe delete
    category = models.CharField(max_length=20, default="pizza")
    checkout = models.ForeignKey(Checkouts, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        name = ", ".join(str(seg) for seg in self.pizza.all())
        top = ", ".join(str(seg) for seg in self.toppings.all())
        if len(top) == 0:
            return f"{name} ${self.price}"
        else:
            return f"{name} ${self.price}\ntoppings: {top}"
        return f"{name} ${self.price}"

class OrderSub(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders_sub')
    sub = models.ManyToManyField(Subs)
    additions = models.ManyToManyField(Addition, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    category = models.CharField(max_length=20, default="sub")
    checkout = models.ForeignKey(Checkouts, on_delete=models.SET_NULL, blank=True, null=True)



    def __str__(self):
        name = ", ".join(str(seg) for seg in self.sub.all())

        return f"{name} ${self.price}"

class OrderPasta(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders_pasta')
    pasta = models.ManyToManyField(Pasta)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    category = models.CharField(max_length=20, default="pasta")
    checkout = models.ForeignKey(Checkouts, on_delete=models.SET_NULL, blank=True, null=True)



    def __str__(self):
        name = ", ".join(str(seg) for seg in self.pasta.all())

        return f"{name} ${self.price}"


class OrderSalad(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders_salad')
    salad = models.ManyToManyField(Salad)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    category = models.CharField(max_length=20, default="salad")
    checkout = models.ForeignKey(Checkouts, on_delete=models.SET_NULL, blank=True, null=True)



    def __str__(self):
        name = ", ".join(str(seg) for seg in self.salad.all())

        return f"{name} ${self.price}"


class OrderPlatter(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders_platter')
    dinner_platter = models.ManyToManyField(Dinner_Platters)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    category = models.CharField(max_length=20, default="platter")
    checkout = models.ForeignKey(Checkouts, on_delete=models.SET_NULL, blank=True, null=True)



    def __str__(self):
        platters = ", ".join(str(seg) for seg in self.dinner_platter.all())

        return f"{platters} ${self.price}"
