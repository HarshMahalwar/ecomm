from cmath import log
from distutils.sysconfig import customize_compiler
from re import X
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json


def store(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = {}
    context = {'products': products, 'orders': items}
    return render(request, 'Home.html', context)


def cart(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        context = {'products': products}
        return render(request, 'Home.html', context)
    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)


def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exists")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or password is invalid.')
    context = {'page': page}
    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('store')


def registerPage(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)
        if user_obj.exists():
            messages.warning(request, 'Email is already registered.')
            return redirect('register')
        user_obj = User.objects.create(
            first_name=first_name, last_name=last_name, email=email, password=password, username=first_name)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, 'Email has been sent to your email account.')
        return redirect('login')
    return render(request, 'register.html')


def checkout(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        context = {'products': products}
        return render(request, 'Home.html', context)
    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)


def update(request):
    data = json.loads(request.body)
    productId = data['productId']

    return JsonResponse('Item was updated', safe=False)


def about(request):
    return redirect('https://harshmahalwar.github.io/portfolio/')


def linkedin(request):
    return redirect('https://www.linkedin.com/in/harsh-mahalwar-4310b316a/')


def github(request):
    return redirect('https://github.com/HarshMahalwar?tab=repositories')
