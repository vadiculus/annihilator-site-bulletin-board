from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('cart_add/<uuid:product_id>', views.cart_add, name='cart_add'),
    path('create_order/', views.send_order, name='create_order'),
    path('requests_to_order/', views.requests_to_order, name='requests_to_order'),
]
