from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path("login", views.login_view, name="login_view"),
    path("create_user", views.create_user, name="create_user"),
    path("login_user", views.login_user, name="login_user"),
    path("logout", views.logout_user, name="logout"),
]
