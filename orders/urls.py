from django.urls import path
# from django

from . import views

app_name = 'orders'
urlpatterns = [
    path("", views.index, name="index"),
]
