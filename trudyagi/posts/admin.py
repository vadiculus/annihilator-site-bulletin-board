from django.contrib import admin
from .models import Product, Review, Rubric, Category, Product_Image

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Rubric)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Product_Image)

# Register your models here.
