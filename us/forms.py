from django import forms
from .models import Contactus, OTP, Resume


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
