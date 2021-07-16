from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_featured']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price','is_featured', 'state', 'date_added']
    list_filter = ['is_featured', 'date_added']
    list_editable = ['price', 'is_featured']
    prepopulated_fields = {'slug': ('name',)}
