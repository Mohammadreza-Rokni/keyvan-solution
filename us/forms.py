from django import forms
from .models import Contactus


class Supplierform(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ['full_name', 'phone_number', 'fieldـofـactivity', 'activityـprovince']

        # error_messages = {
            
        # }




class Jobseekerform(forms.ModelForm):
    class Meta:
        model = Contactus
        exclude = ['full_name', 'phone_number', 'fieldـofـactivity', 'activityـprovince']

        # error_messages = {
            
        # }