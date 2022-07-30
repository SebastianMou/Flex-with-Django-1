# Generated by Django 3.1.4 on 2022-07-29 01:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Shop', '0003_auto_20220609_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPlantillas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_p', models.CharField(db_index=True, max_length=255)),
                ('slug_p', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categoriesplantillas',
            },
        ),
        migrations.CreateModel(
            name='ProductPlantillas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_p', models.CharField(max_length=255)),
                ('author_p', models.CharField(default='admin', max_length=255)),
                ('description_p', tinymce.models.HTMLField(blank=True)),
                ('image_p', models.ImageField(default='images/default.png', upload_to='images/')),
                ('slug_p', models.SlugField(max_length=255)),
                ('price_p', models.DecimalField(decimal_places=2, max_digits=7)),
                ('old_price_p', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('in_stock_p', models.BooleanField(default=True)),
                ('is_active_p', models.BooleanField(default=True)),
                ('created_p', models.DateTimeField(auto_now_add=True)),
                ('updated_p', models.DateTimeField(auto_now=True)),
                ('category_plantillas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productplantillas', to='Shop.categoryplantillas')),
                ('created_by_p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_creator_p', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Productplantillas',
            },
        ),
    ]
