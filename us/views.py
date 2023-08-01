from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from .models import Customer, Contactus, Aboutus
from .forms import Jobseekerform, Supplierform
# Create your views here.

class Career(TemplateView):
    template_name = 'index.html'


class Customers(DetailView):
    template_name = 'index.html'
    model = Customer


class ContactUs(DetailView):
    template_name = 'index.html'
    model = Contactus

    def get(self, request):
        form = Jobseekerform() and Supplierform()

        return render(request, "html page" , {
            "form" : form
        })


    def post(self, request):
        form = Jobseekerform(request.POST) and Supplierform(request.POST)

        if form.is_valid():
            form.save()
            return redirect("html page")
        
        return render(request, "html page" , {
            "form" : form
        })
        


class AboutUs(DetailView):
    template_name = 'index.html'
    model = Aboutus