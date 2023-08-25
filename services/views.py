from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from .models import Oursolutions, Ourservices, Ourproducts, Article
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'services/blog.html'
    context_object_name = "articles"

    def get_queryset(self):
        queryset = super().get_queryset()

        sort = self.request.GET.get('sort')
        if sort == 'newest':
            queryset = queryset.order_by('-publish', '-update')
        elif sort == 'oldest':
            queryset = queryset.order_by('publish', 'update')

        return queryset
    

class ArticleDetailView(DetailView):
    template_name = 'services/blog_detail.html'
    model = Article



class OurSolutionsListView(ListView):
    model = Oursolutions
    template_name = 'services/solutions.html'
    context_object_name = "oursolutions"



# class OurSolutionsDetailView(DetailView):
#     template_name = 'index.html'
#     model = Oursolutions


class OurServicesListView(ListView):
    model = Ourservices
    template_name = 'services/services.html'
    context_object_name = "ourservices"


# class OurServicesDetailView(DetailView):
#     template_name = 'index.html'
#     model = Ourservices


class OurProductsListView(ListView):
    model = Ourproducts
    template_name = 'services/product.html'
    context_object_name = "ourproducts"



# class OurProductsDetailView(DetailView):
#     template_name = 'index.html'
#     model = Ourproducts
