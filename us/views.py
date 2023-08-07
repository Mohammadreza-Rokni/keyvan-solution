from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Customer, Contactus, Aboutus, Career, OTP
from .forms import JobSeekerForm, SupplierForm
from random import randint
import ghasedakpack


SMS = ghasedakpack.Ghasedak("3f37ee30f4690b3334c5e3552b67615a4171d8a1f2ed7444efb87b628bd53e9b")


class Career(DetailView):
    template_name = 'index.html'
    model = Career

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

    def post(self, request):
        jobseeker_form = JobSeekerForm(request.POST)
        supplier_form = SupplierForm(request.POST)
        
        if jobseeker_form.is_valid() and supplier_form.is_valid():
            jobseeker_random_code = randint(1000, 9999)
            jobseeker_cd = jobseeker_form.cleaned_data
            SMS.verification(
                {'receptor': jobseeker_cd["phone_number"], 'type': '1', 'template': 'Your Template', 'param1': jobseeker_random_code}
            )
            jobseeker_form.instance.verification_code = OTP.objects.create(phone=jobseeker_cd["phone_number"], code=jobseeker_random_code)
            jobseeker_form.save()

            supplier_random_code = randint(1000, 9999)
            supplier_cd = supplier_form.cleaned_data
            SMS.verification(
                {'receptor': supplier_cd["phone_number"], 'type': '1', 'template': 'Your Template', 'param1': supplier_random_code}
            )
            supplier_form.instance.verification_code = OTP.objects.create(phone=supplier_cd["phone_number"], code=supplier_random_code)
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