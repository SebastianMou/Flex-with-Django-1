from django.urls import path
from . import views

app_name = 'Shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('articulo/<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path('freelancer/', views.freelancer, name='freelancer'),
    path('plantillas/', views.plantillas, name='plantillas'),
    path('plantillas_todas/<slug:plantillas_slug>', views.plantillas_detail, name='plantillas_detail'),
    path('shop_plantilla/<slug:plantilla_category_slug>/', views.plantilla_category_list, name='plantilla_category_list'),

]
