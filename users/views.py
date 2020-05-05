from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from .forms import CreateUser
# Create your views here.

def register(request):
    print("\n\nBlablabla\n\n")
    if request.method == 'POST':
        print("\n\nrequest method is post\n\n")
        register_form = CreateUser(request.POST)
        print(f"\nform:\n{register_form}\n\n")
        if register_form.is_valid():
            print("\n\nform is valid\n\n")
            register_form.save()
            username = register_form.cleaned_data.get("username")
            password = register_form.clean_password2()
            print(f"\n\n{username}\n{password}\n")
            user = authenticate(request, username=username, password=password)
            print(f"\nafter authenticate\n{user}\n\n")
            login(request, user)
            print("\n\nuser logged in\n\n")
            return redirect("orders:index")

    else:
        print("\n\nelse ran\n\n")
        register_form = CreateUser()
    return render(request, "users/register.html", {"register_form": register_form})

def login_view(request):
    print(f"\n\nlogin view ran\n\n")
    register_form = CreateUser()
    login_form = AuthenticationForm()
    return render(request, "users/login.html", {"login_form": login_form, "register_form": register_form})

def logout_user(request):
    logout(request)
    return redirect('orders:index')

def login_user(request):
    print("\nin login user\n")
    if request.method == 'POST':
        print("\nsurvived if clause\n")
        login_form = AuthenticationForm(request.POST)
        register_form = CreateUser(request.POST)
        print(f"\nlogin_form:\n{login_form}\n\n")
        print(f"\nregister_form:\n{register_form}\n\n")
        if login_form.is_valid():
            login(request, user)
            print(f"\nuser:\n{user}\n\n")
            return redirect("orders:index")

    else:
        form = AuthenticationForm()
    return redirect("orders:index")
