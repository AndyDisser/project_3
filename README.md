# Project 3

Web Programming with Python and JavaScript

The Project is divided into two apps:

    users
    orders

Users handles the authentication of the users as well as the login and logout
process. Orders handles the rest of the app.
In index.html you find the menu of pizzeria. You are also able the add items to
the cart and edit your cart. When a user submits an order he is sent to confirm.html.
It contains a simple listing of all the items in the cart, so he can check them
again before finally submitting the order.
Once a user has submitted a order he can see the status of that order,
as well as all of his older orders in view_own_orders.html.
The owner on the other hand has the opportunity to see in all_orders_guests.html
every order submitted. There he can also mark orders as delivered, so that
the customer gets an update on his order.
All those templates are extended by base.html, which includes the a basic
navigation bar as well as the background picture of Pinocchios Pizza.

The personal touch of the project is that every user has the opportunity to
see all of his previous orders as well as their status.
