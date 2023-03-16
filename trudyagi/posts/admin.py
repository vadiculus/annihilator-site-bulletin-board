from django.contrib import admin
from .models import Product, Review, Rubric, Category, Product_Image

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Rubric)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)
admin.site.register(Product_Image)

# Register your models here.
