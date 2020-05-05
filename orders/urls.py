from django.urls import path
# from django

from . import views

app_name = 'orders'
urlpatterns = [
    path("", views.index, name="index"),
    path("cart/", views.add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<str:category>/<str:pk>", views.remove_from_cart, name="remove_from_cart"),
    path("confirm/", views.confirm_view, name="confirm_view"),
    path("checkout/", views.confirm_order, name="confirm_order"),
    path("view_all_orders/", views.view_all_orders, name="view_all_orders"),
    path("view_own_orders/", views.view_own_orders, name="view_own_orders"),
    path("mark_as_delivered/<str:order_id>", views.mark_as_delivered, name="mark_as_delivered")
]
