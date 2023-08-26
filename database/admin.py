from django.contrib import admin

from database.models import Product, Category, Version

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'decrp',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'number',)
    list_filter = ('name',)

