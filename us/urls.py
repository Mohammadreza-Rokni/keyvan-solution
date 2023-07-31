from django.urls import path
from . import views

app_name = 'us'
urlpatterns = [
    path("", views.Career.as_view(), name='career'),
    path("", views.Customers.as_view(), name='customers'),
    path("", views.Contactus.as_view(), name='contactus'),
    path("", views.AboutUs.as_view(), name='aboutus'),
]