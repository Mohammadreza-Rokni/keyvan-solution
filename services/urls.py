from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path("", views.OurSolutions.as_view(), name='oursolutions'),
    path("", views.OurServices.as_view(), name='ourservices'),
    path("", views.OurProducts.as_view(), name='ourproducts'),
]