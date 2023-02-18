from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('rubrics/<slug:rubric_slug>', views.get_by_rubric, name='rubrics'),
    path('product/<uuid:product_unique_id>', views.product, name='product_detail'),
    path('add_product/', views.CreateProductView.as_view(), name='add-product'),
    path('search-product-data/', views.search_product_data, name='search_product_data'),
    path('search-product/', views.search_product, name='search_product'),
    path('delete-review/<int:review_id>', views.delete_review, name='delete_review'),
    path('delete-product/<uuid:pk>', views.DeleteProductView.as_view(), name='delete_product'),
    path('update-product/<uuid:pk>', views.UpdateProductView.as_view(), name='update_product'),
]
