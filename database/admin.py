from django.contrib import admin

from database.models import Product, Version, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'cat',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'cat','img',)
    list_filter = ('cat',)
    search_fields = ('name', 'decrp',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'number',)
    list_filter = ('name',)

