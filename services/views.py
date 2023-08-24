from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView
from .models import Oursolutions, Ourservices, Ourproducts, Article, Category
# Create your views here.


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    paginate_by = 4


class ArticleDetailView(DetailView):
    template_name = 'index.html'
    model = Article


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, 'index.html', {'articles': articles})


class OurSolutionsListView(ListView):
    model = Oursolutions
    context_object_name = "oursolutions"
    paginate_by = 4


class OurSolutionsDetailView(DetailView):
    template_name = 'index.html'
    model = Oursolutions


class OurServicesListView(ListView):
    model = Ourservices
    context_object_name = "ourservices"
    paginate_by = 4


class OurServicesDetailView(DetailView):
    template_name = 'index.html'
    model = Ourservices


class OurProductsListView(ListView):
    model = Ourproducts
    context_object_name = "ourproducts"
    paginate_by = 4


class OurProductsDetailView(DetailView):
    template_name = 'index.html'
    model = Ourproducts
