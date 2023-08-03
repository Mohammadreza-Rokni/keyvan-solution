from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path("articleslist", views.ArticleListView.as_view(), name='article_list'),
    path("articledetail/<str:slug>", views.ArticleDetailView.as_view(), name='articles_detail'),
    path("category/<int:pk>", views.category_detail, name='category_detail'),
    path("solutionslist", views.OurSolutionsListView.as_view(), name='oursolutions_list'),
    path("solutiondetail/<str:slug>", views.OurSolutionsDetailView.as_view(), name='oursolution_detail'),
    path("serviceslist", views.OurServicesListView.as_view(), name='ourservices_list'),
    path("servicedetail/<str:slug>", views.OurServicesDetailView.as_view(), name='ourservice_detail'),
    path("productslist", views.OurProductsListView.as_view(), name='ourproducts_list'),
    path("productdetail/<str:slug>", views.OurProductsDetailView.as_view(), name='ourproduct_detail'),
]