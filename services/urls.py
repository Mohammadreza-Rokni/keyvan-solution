from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path("articleslist", views.ArticleListView.as_view(), name='article_list'),
    path("articledetail/<str:slug>",
         views.ArticleDetailView.as_view(), name='articles_detail'),
    path("solutionslist", views.OurSolutionsListView.as_view(),
         name='oursolutions_list'),
    path("serviceslist", views.OurServicesListView.as_view(),
         name='ourservices_list'),
    path("productslist", views.OurProductsListView.as_view(),
         name='ourproducts_list'),
    path('search/', views.search, name='search_blog'),
]
