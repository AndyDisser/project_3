from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from .forms import CreateUser
# Create your views here.

def create_user(request):
    print("\n\nBlablabla\n\n")
    if request.method == 'POST':
        form = CreateUser(request.POST)
        print(f"\n\n{form}\n\n")
        if form.is_valid():
            print("\n\nform is valid\n\n")
            form.save()
            username = form.cleaned_data.get("username")
            password = form.clean_password2()
            print(f"\n\n{username}\n{password}\n")
            user = authenticate(request, username=username, password=password)
            print(f"\nafter authenticate\n{user}\n\n")
            login(request, user)
            print("\n\nuser logged in\n\n")
            return redirect("orders:index")

    else:
        print("\n\nelse ran\n\n")
        register_form = CreateUser()
    return render(request, "users/login.html", {"register_form": register_form})

def login_view(request):
    print(f"\n\nlogin view ran\n\n")
    register_form = CreateUser()
    # login_form = AuthenticationForm()
    return render(request, "users/login.html", {"login_form": AuthenticationForm(), "register_form": register_form})

def logout_user(request):
    logout(request)
    return redirect('orders:index')

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, user)
            return redirect("orders:index")

    else:
        form = AuthenticationForm()
    return redirect("orders:index")
