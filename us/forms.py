from django import forms
from .models import Contactus, OTP, Resume
from django.core import validators


class OTPForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), validators=[validators.MaxLengthValidator(11)])


class CheckOTPForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), validators=[validators.MaxLengthValidator(4)])


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ['full_name', 'phone_number', 'field_of_activity',
                  'activity_province', 'verification_code']


class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = Contactus
        exclude = ['full_name', 'phone_number',
                   'field_of_activity', 'activity_province']


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('title', 'resume',)
