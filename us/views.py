from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import customers
# Create your views here.

class Career(TemplateView):
    template_name = 'index.html'

class Customers(DetailView):
    template_name = 'index.html'
    model = customers