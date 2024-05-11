from django.contrib import admin

from .models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name'  , 'slug']  # for display field  in admin panel
    prepopulated_fields = ({'slug': ('name',)})  # auto population


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']  # for filter the data in admin panel
    list_editable = ['price', 'in_stock']  # for edit the data directly in admin panel
    prepopulated_fields = ({'slug': ('title' ,)})
