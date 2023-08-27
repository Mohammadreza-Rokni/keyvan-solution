from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
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
    context_object_name = "services"


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

def search(request): 
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    if not objects_list:
        return render(request, '404/404.html')
    return render(request, 'services/blog.html', {'articles': objects_list})
