from django import forms
from .models import Contactus


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ['full_name', 'phone_number', 'field_of_activity', 'activity_province']

class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = Contactus
        exclude = ['full_name', 'phone_number', 'field_of_activity', 'activity_province']
