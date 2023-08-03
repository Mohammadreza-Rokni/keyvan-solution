from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Oursolutions, Ourservices, Ourproducts, Article
# Create your views here.
class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    paginate_by = 4


class OurSolutionsList(ListView):
    model = Oursolutions
    context_object_name = "oursolutions"
    paginate_by = 1

class OurSolutionsDetail(DetailView):
    template_name = 'index.html'
    model = Oursolutions



class OurServices(DetailView):
    template_name = 'index.html'
    model = Ourservices

class OurProducts(DetailView):
    template_name = 'index.html'
    model = Ourproducts