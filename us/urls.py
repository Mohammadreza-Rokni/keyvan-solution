from django.urls import path
from . import views

app_name = 'us'
urlpatterns = [
    path("jobposition/", views.JobposView.as_view(), name='jobpos'),
    path("customers/", views.CustomersView.as_view(), name='customers'),
    path("contactus/", views.ContactUsView.as_view(), name='contactus'),
    path("aboutus/", views.AboutUsView.as_view(), name='aboutus'),
]
