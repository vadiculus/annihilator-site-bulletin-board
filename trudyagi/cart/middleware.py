from django.utils.deprecation import MiddlewareMixin
from .cart import Cart

class CartMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.cart = Cart(request)
        if request.user.is_authenticated:
            request.new_messages_count = request.user.seller_orders.filter(read=False).count()
        response = self.get_response(request)
        return response