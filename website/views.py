from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'website/index.html')


def products(request):
    return render(request, 'website/products.html')


def about_us(request):
    return render(request, 'website/about_us.html')


def contact(request):
    return render(request, 'website/contact.html')
