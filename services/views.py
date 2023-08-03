from django.shortcuts import render
from django.views.generic import DetailView
from .models import Oursolutions, Ourservices, Ourproducts
# Create your views here.
class OurSolutions(DetailView):
    template_name = 'index.html'
    model = Oursolutions

class OurServices(DetailView):
    template_name = 'index.html'
    model = Ourservices

class OurProducts(DetailView):
    template_name = 'index.html'
    model = Ourproducts