from django.contrib import admin
from .models import Category, Product, ProductPlantillas, CategoryPlantillas
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


# Register your models here.
admin.site.site_header = 'Ensocio.mx admin'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'old_price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'old_price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'author')
    list_filter = ('title', 'author')

@admin.register(CategoryPlantillas)
class CategoryPlantillasAdmin(admin.ModelAdmin):
    list_display = ['name_p', 'slug_p']
    prepopulated_fields = {'slug_p': ('name_p',)}
    search_fields = ('name_p', 'slug_p')
    list_filter = ('name_p', 'slug_p')

@admin.register(ProductPlantillas)
class ProductPlantillasAdmin(admin.ModelAdmin):
    list_display = ['title_p', 'author_p', 'slug_p', 'price_p', 'old_price_p', 'in_stock_p', 'created_p', 'updated_p']
    list_filter = ['in_stock_p', 'is_active_p']
    list_editable = ['price_p', 'old_price_p', 'in_stock_p']
    prepopulated_fields = {'slug_p': ('title_p',)}
    search_fields = ('title_p', 'author_p')
    list_filter = ('title_p', 'author_p')
