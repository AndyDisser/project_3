from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Pizza, Toppings, Subs, Addition, Pasta, Salad, Dinner_Platters

def index(request):
    context = {
        "pizzas": Pizza.objects.all(),
        "toppings": Toppings.objects.all(),
        "subs": Subs.objects.all(),
        "additions": Addition.objects.all(),
        "pastas": Pasta.objects.all(),
        "salads": Salad.objects.all(),
        "dinner_platters": Dinner_Platters.objects.all()
    }
    if not request.user.is_authenticated:
        user = request.user
        context.update({"user": user})
    return render(request, "orders/index.html", context)
