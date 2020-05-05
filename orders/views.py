from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import OrderPizzaForm, ToppingsForm, PizzaFrom

from .models import Pizza, Toppings, Subs, Addition, Pasta, Salad, Dinner_Platters, OrderPizza, OrderSub, OrderSalad, OrderPasta, OrderPlatter, Checkouts

def index(request):

    #get all Orders
    context = {
        "pizzas": Pizza.objects.all(),
        "toppings": Toppings.objects.all(),
        "subs": Subs.objects.all(),
        "additions": Addition.objects.all(),
        "pastas": Pasta.objects.all(),
        "salads": Salad.objects.all(),
        "dinner_platters": Dinner_Platters.objects.all(),
    }

    if request.user.is_authenticated:
        user = request.user
        orders_pizza = OrderPizza.objects.filter(user=user, ordered=False, delivered=False)
        orders_subs = OrderSub.objects.filter(user=user, ordered=False, delivered=False)
        orders_pasta = OrderPasta.objects.filter(user=user, ordered=False, delivered=False)
        orders_salad = OrderSalad.objects.filter(user=user, ordered=False, delivered=False)
        orders_platter = OrderPlatter.objects.filter(user=user, ordered=False, delivered=False)
        list_all_orders_cart = [orders_pizza, orders_subs, orders_pasta, orders_salad, orders_platter]

        total_cost = 0
        count = 0
        list_items_cart = []
        for i in list_all_orders_cart:
            for j in i:
                count += 1
                try:
                    total_cost += j.price
                except Exception:
                    pass
                list_items_cart.append(j)
                # print(j)
        num_cart_items = count
        user = request.user
        context.update({"num_cart_items": num_cart_items,
                        "list_items_cart": list_items_cart,
                        "total_cost": total_cost,
                        "user": user})
    return render(request, "orders/index.html", context)


def add_to_cart(request):
    print("\n\nin add to cart\n\n")

    user = request.user
    category = request.POST.get("category", None)

    # Order Pizza
    if category == "sic" or category == "reg":
        toppings = request.POST.getlist("toppings", None)
        pizza_id = request.POST.get("submit-button", None)
        price = request.POST.get("options", None)

        # print(f"\ncategory:\n{category}\n\n")
        # print(f"\ntoppings:\n{toppings}\n\n")
        # print(f"\npizza_id:\n{pizza_id}\n\n")
        # print(f"\nprice:\n{price}\n\n")

        pizza = Pizza.objects.get(id=pizza_id)
        # print(f"\n\npizza:\n{pizza}\n\n")

        # # could be that i need to use multiple toppings in the cart to refert to
        # # the multiple possible toppings
        user = request.user
        instance = OrderPizza.objects.create(user=user, price=price)

        # use add for single instances
        instance.pizza.add(pizza)

        if toppings is not None:
            # print(toppings)
            # toppings = list(toppings)
            for i in range(len(toppings)):
                toppings[i] = Toppings.objects.get(pk=toppings[i])
            # use set for lists
            instance.toppings.set(toppings)

    # Order Sub
    elif category == "subs":
        addition = request.POST.getlist("addition", None)
        price = request.POST.get("options", None)
        sub_id = request.POST.get("submit-button", None)
        sub = Subs.objects.get(id=sub_id)

        user = request.user
        instance = OrderSub.objects.create(user=user, price=price)
        instance.sub.add(sub)

        cost_additions = 0
        if addition is not None and len(addition) > 0:
            print("blank is not none")
            print(addition)
            num_additons = len(addition)
            cost_additions += (num_additons * 0.5)
            for i in range(len(addition)):
                addition[i] = Addition.objects.get(id=addition[i])
                print(addition)
            if num_additons > 1:
                instance.additons.set(addition)
            else:
                addition = addition[0]
                instance.additions.add(addition)
        print("additions is none")
    # Order Pasta
    elif category == "pasta":
        pasta_id = request.POST.get("submit-button", None)

        if pasta_id is not None:
            pasta = Pasta.objects.get(pk=pasta_id)

        price = pasta.price

        instance = OrderPasta.objects.create(user=user, price=price)
        instance.pasta.add(pasta)


    # Order Salad
    elif category == "salad":
        salad_id = request.POST.get("submit-button", None)
        if salad_id is not None:
            salad = Salad.objects.get(pk=salad_id)
            price = salad.price
            instance = OrderSalad.objects.create(user=user, price=price)
            instance.salad.add(salad)

    # Order Platter
    elif category == "platter":
        platter_id = request.POST.get("submit-button", None)
        if platter_id is not None:
            platter = Dinner_Platters.objects.get(pk=platter_id)
            price = request.POST.get("options", None)

            instance = OrderPlatter.objects.create(user=user, price=price)
            instance.dinner_platter.add(platter)

    return redirect('orders:index')

def remove_from_cart(request, category, pk):
    # print(f"\nremove_from_cart\n{category}\n\n")
    if category == "pizza":
        OrderPizza.objects.filter(pk=pk).delete()
    elif category == "sub":
        OrderSub.objects.filter(pk=pk).delete()
    elif category == "pasta":
        OrderPasta.objects.filter(pk=pk).delete()
    elif category == "salad":
        OrderSalad.objects.filter(pk=pk).delete()
    elif category == "platter":
        OrderPlatter.objects.filter(pk=pk).delete()
    return redirect('orders:index')

def confirm_view(request):
    user = request.user
    orders_pizza = OrderPizza.objects.filter(user=user, ordered=False, delivered=False)
    orders_subs = OrderSub.objects.filter(user=user, ordered=False, delivered=False)
    orders_pasta = OrderPasta.objects.filter(user=user, ordered=False, delivered=False)
    orders_salad = OrderSalad.objects.filter(user=user, ordered=False, delivered=False)
    orders_platter = OrderPlatter.objects.filter(user=user, ordered=False, delivered=False)
    list_all_orders_cart = [orders_pizza, orders_subs, orders_pasta, orders_salad, orders_platter]


    total_cost = 0
    count = 0
    list_items_cart = []
    for i in list_all_orders_cart:
        for j in i:
            count += 1
            try:
                total_cost += j.price
            except Exception:
                pass
            list_items_cart.append(j)

    context = {
    "list_items_cart": list_items_cart,
    "total_cost": total_cost
    }
    return render(request, "orders/confirm.html", context)

def confirm_order(request):
    user = request.user
    print(f"in confirm order")
    user = request.user
    orders_pizza = OrderPizza.objects.filter(user=user, ordered=False, delivered=False)
    orders_subs = OrderSub.objects.filter(user=user, ordered=False, delivered=False)
    orders_pasta = OrderPasta.objects.filter(user=user, ordered=False, delivered=False)
    orders_salad = OrderSalad.objects.filter(user=user, ordered=False, delivered=False)
    orders_platter = OrderPlatter.objects.filter(user=user, ordered=False, delivered=False)
    list_all_orders_cart = [orders_pizza, orders_subs, orders_pasta, orders_salad, orders_platter]

    checkout = Checkouts.objects.create(user=user)
    checkout.save()
    for list in list_all_orders_cart:
        for item in list:
            try:
                print(item)
                print(item.ordered)
                item.ordered = True
                item.checkout = checkout
                print(item.ordered)
                item.save()
            except Exception:
                print("\n\nsome error occured\n\n")

    return redirect('orders:index')

def view_all_orders(request):
    list_orders = Checkouts.objects.all()
    context = {
        "list_orders": list_orders
    }
    return render(request, "orders/all_orders_guests.html", context)

def view_own_orders(request):
    # write code that each customer can see their order history and status
    user = request.user
    checkouts = Checkouts.objects.filter(user=user)
    print(f"\n\ncheckouts:\n{checkouts}\n\n")
    context = {
        "checkouts": checkouts
    }
    return render(request, 'orders/view_own_orders.html', context)

def mark_as_delivered(request, order_id):
    order = Checkouts.objects.get(id=order_id)
    order.delivered = True
    order.save()
    return redirect('orders:view_all_orders')
