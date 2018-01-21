from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated', 'authentication_required']
    list_filter = ['available', 'created', 'updated', 'category', 'authentication_required']
    list_editable = ['price', 'stock', 'available', 'authentication_required']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
