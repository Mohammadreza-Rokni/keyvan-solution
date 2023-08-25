from django.shortcuts import render
from django.views.generic import ListView
from services.models import Article
# Create your views here.

class HomeListView(ListView):
    template_name = 'home/home.html'
    model = Article
    context_object_name = "articles"

    # def get_queryset(self):
    #     queryset = super().get_queryset()

    #     sort = self.request.GET.get('sort')
    #     if sort == 'newest':
    #         queryset = queryset.order_by('-publish', '-update')
    #     elif sort == 'oldest':
    #         queryset = queryset.order_by('publish', 'update')

    #     return queryset