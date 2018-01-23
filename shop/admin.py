from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated', 'authentication_required', 'online_course_dispatch']
    list_filter = ['available', 'created', 'updated', 'category', 'authentication_required', 'online_course_dispatch']
    list_editable = ['price', 'stock', 'available', 'authentication_required', 'online_course_dispatch']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
