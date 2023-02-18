from django.contrib import admin
from .models import Product, Review, Rubric, Category, Product_Image

admin.site.register(Product)
admin.site.register(Rubric)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Product_Image)

# Register your models here.
