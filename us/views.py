from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Customer, Contactus, Aboutus
# Create your views here.

class Career(TemplateView):
    template_name = 'index.html'

class Customers(DetailView):
    template_name = 'index.html'
    model = Customer

class ContactUs(DetailView):
    template_name = 'index.html'
    model = Contactus

class AboutUs(DetailView):
    template_name = 'index.html'
    model = Aboutus