from email.policy import default
from django.conf import settings
from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models

# Create your models here.
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('Shop:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = tinymce_models.HTMLField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    old_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('Shop:product_detail', args=[self.slug])

    def __str__(self):
        return self.title

class CategoryPlantillas(models.Model):
    name_p = models.CharField(max_length=255, db_index=True)
    slug_p = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categoriesplantillas'

    def get_absolute_url(self):
        return reverse('Shop:plantilla_category_list', args=[self.slug_p])

    def __str__(self):
        return self.name_p

class ProductPlantillas(models.Model):
    category_plantillas = models.ForeignKey(CategoryPlantillas, related_name='productplantillas', on_delete=models.CASCADE)
    created_by_p = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator_p')
    title_p = models.CharField(max_length=255)
    author_p = models.CharField(max_length=255, default='admin')
    description_p = tinymce_models.HTMLField(blank=True)
    image_p0 = models.ImageField(upload_to='images/', default='images/default.png', null=True)
    image_p1 = models.ImageField(upload_to='images/', default='images/default.png', null=True)
    image_p2 = models.ImageField(upload_to='images/', default='images/default.png', null=True)
    slug_p = models.SlugField(max_length=255)
    price_p = models.DecimalField(max_digits=7, decimal_places=2)
    old_price_p = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    in_stock_p = models.BooleanField(default=True)
    is_active_p = models.BooleanField(default=True)
    created_p = models.DateTimeField(auto_now_add=True)
    updated_p = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Productplantillass'
        #ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('Shop:plantillas_detail', args=[self.slug_p])

    def __str__(self):
        return self.title_p
