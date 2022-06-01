from django.contrib import admin
from .models import Category, Product
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
