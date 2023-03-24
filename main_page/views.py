from django.shortcuts import render, redirect
from .models import Service

from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'employee', 'service', 'date']


def home_page(request):
    return render(request, "home.html")


def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})


def contacts(request):
    return render(request, 'contacts.html')


def orders(request):
    services = Order.objects.all()
    return render(request, 'order_list.html', {'services': services})
