from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from uuid import uuid4
from django.views.generic import DetailView, ListView, FormView, UpdateView, View
from .models import Customer, Contactus, Aboutus, JobPos, OTP, Resume
from .forms import JobSeekerForm, SupplierForm, ResumeForm, OTPForm, CheckOTPForm
from random import randint
import requests
import ghasedakpack


SMS = ghasedakpack.Ghasedak(
    "3f37ee30f4690b3334c5e3552b67615a4171d8a1f2ed7444efb87b628bd53e9b")


class JobposView(ListView):
    template_name = 'us/jobposition.html'
    model = JobPos
    context_object_name = 'jobs'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not queryset.exists():
            # If no JobPos exists, render notjobpos.html
            self.template_name = 'us/notjobpos.html'
        return queryset


class JobDeatailView(UpdateView):
    template_name = 'us/jobposdetail.html'
    model = JobPos
    form_class = ResumeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ResumeForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume_file = form.cleaned_data['resume']

            Resume.objects.create(
                job_position=self.object,
                title=form.cleaned_data['title'],
                resume=resume_file
            )

            return redirect('us:jobdetail', slug=self.object.slug)
        else:
            print(form.errors)
            context = self.get_context_data(object=self.object, form=form)
            return self.render_to_response(context)

    # def get(self, request):
    #     form = SupplierForm()
    #     return render(request, "html_page.html", {
    #         "form": form
    #     })

    # def post(self, request):
    #     form = SupplierForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("html_page")
    #     return render(request, "html_page.html", {
    #         "form": form
    #     })


class CustomersView(ListView):
    template_name = 'us/customers.html'
    model = Customer
    context_object_name = 'customers'


class ContactUsView(ListView):
    template_name = 'us/contactus.html'
    model = Contactus

    # def post(self, request):
    #     jobseeker_form = JobSeekerForm(request.POST)
    #     supplier_form = SupplierForm(request.POST)

    #     if jobseeker_form.is_valid() and supplier_form.is_valid():
    #         jobseeker_random_code = randint(1000, 9999)
    #         jobseeker_cd = jobseeker_form.cleaned_data
    #         SMS.verification(
    #             {'receptor': jobseeker_cd["phone_number"], 'type': '1',
    #                 'template': 'Your Template', 'param1': jobseeker_random_code}
    #         )
    #         jobseeker_form.instance.verification_code = OTP.objects.create(
    #             phone=jobseeker_cd["phone_number"], code=jobseeker_random_code)
    #         jobseeker_form.save()

    #         supplier_random_code = randint(1000, 9999)
    #         supplier_cd = supplier_form.cleaned_data
    #         SMS.verification(
    #             {'receptor': supplier_cd["phone_number"], 'type': '1',
    #                 'template': 'Your Template', 'param1': supplier_random_code}
    #         )
    #         supplier_form.instance.verification_code = OTP.objects.create(
    #             phone=supplier_cd["phone_number"], code=supplier_random_code)
    #         supplier_form.save()

    #         return redirect("home:home")

    #     return render(request, "us/workus.html", {
    #         "jobseeker_form": jobseeker_form,
    #         "supplier_form": supplier_form
    #     })


class OTPView(View):

    def get(self, request):
        template_name = 'us/otp.html'
        form = OTPForm()
        return render(request, 'us/otp.html', {'form': form})

    def post(self, request):
        form = OTPForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000, 9999)
            SMS.verification(
                {'receptor': cd["phone"], 'type': '1',
                 'template': 'randcode', 'param1': randcode}
            )
            token = str(uuid4())
            OTP.objects.create(phone=cd['phone'], code=randcode, token=token)
            print(randcode)
            return redirect(reverse('us:checkotp') + f"?token={token}")

        else:
            form.add_error("phone", "invalid datat")

        return render(request, 'us/otp.html', {'form': form})


class CheckOTPView(View):
    def get(self, request):
        template_name = 'us/checkotp.html'
        form = CheckOTPForm()
        return render(request, 'us/checkotp.html', {'form': form})

    def post(self, request):
        token = request.GET.get('token')
        form = CheckOTPForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if OTP.objects.filter(code=cd['code'], token=token).exists():
                otp = OTP.objects.get(token=token)
                otp.delete()
                return redirect('home:home')

        else:
            form.add_error("phone", "invalid data")

        return render(request, 'us/checkotp.html', {'form': form})


class AboutUsView(ListView):
    template_name = 'us/aboutus.html'
    model = Aboutus
