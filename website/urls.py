from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('about_us', views.about_us, name='about_us'),
    path('contact', views.contact, name='contact'),
]
