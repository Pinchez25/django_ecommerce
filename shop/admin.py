from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from .models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(Product)
class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['title', 'category', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'available']
    search_fields = ['title', 'slug']
