from django import forms
from .models import Contactus, OTP, Resume
from django.core import validators


class OTPForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), validators=[validators.MaxLengthValidator(11)])


class CheckOTPForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), validators=[validators.MaxLengthValidator(4)])


class WorkWithUsForm(forms.ModelForm):
    class Meta:
        model = Contactus
        exclude = ['verification_code', 'created']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-control custom-input'}),
            'landlineـphone': forms.TextInput(attrs={'class': 'form-control custom-input', 'type': 'tel'}),
            'cellular_phone': forms.TextInput(attrs={'class': 'form-control custom-input', 'type': 'tel'}),
            'field_of_activity': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'prudoct': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'state': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'city': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'address': forms.TextInput(attrs={'class': 'form-control custom-input'}),
        }


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('title', 'resume',)


# class JobSeekerForm(forms.ModelForm):
#     class Meta:
#         model = Contactus
#         exclude = ['full_name', 'phone_number',
#                    'field_of_activity', 'activity_province']


# class SupplierForm(forms.ModelForm):
#     class Meta:
#         model = Contactus
#         fields = ['full_name', 'phone_number', 'field_of_activity',
#                   'activity_province', 'verification_code']
