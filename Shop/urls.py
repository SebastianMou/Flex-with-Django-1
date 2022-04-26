from django.urls import path
from . import views

app_name = 'Shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('articulo/<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]
