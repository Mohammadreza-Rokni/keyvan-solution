from django.urls import path
from . import views

app_name = 'us'
urlpatterns = [
    path("career/", views.Career.as_view(), name='career'),
    path("custumers/", views.CustomersView.as_view(), name='customers'),
    path("contactus/", views.ContactUsView.as_view(), name='contactus'),
    path("aboutus/", views.AboutUsView.as_view(), name='aboutus'),
]
