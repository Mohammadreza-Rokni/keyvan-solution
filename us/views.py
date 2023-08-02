from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from .models import Customer, Contactus, Aboutus
from .forms import JobSeekerForm, SupplierForm

class Career(TemplateView):
    template_name = 'index.html'

class Customers(DetailView):
    template_name = 'index.html'
    model = Customer

    def get(self, request):
        form = SupplierForm()
        return render(request, "html_page.html", {
            "form": form
        })

    def post(self, request):
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("html_page")
        return render(request, "html_page.html", {
            "form": form
        })

class ContactUs(DetailView):
    template_name = 'index.html'
    model = Contactus

    def get(self, request):
        jobseeker_form = JobSeekerForm()
        supplier_form = SupplierForm()
        return render(request, "html_page.html", {
            "jobseeker_form": jobseeker_form,
            "supplier_form": supplier_form
        })

    def post(self, request):
        jobseeker_form = JobSeekerForm(request.POST)
        supplier_form = SupplierForm(request.POST)
        
        if jobseeker_form.is_valid() and supplier_form.is_valid():
            jobseeker_form.save()
            supplier_form.save()
            return redirect("html_page")
        
        return render(request, "html_page.html", {
            "jobseeker_form": jobseeker_form,
            "supplier_form": supplier_form
        })

class AboutUs(DetailView):
    template_name = 'index.html'
    model = Aboutus

    def get(self, request):
        form = SupplierForm()
        return render(request, "html_page.html", {
            "form": form
        })

    def post(self, request):
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("html_page")
        return render(request, "html_page.html", {
            "form": form
        })