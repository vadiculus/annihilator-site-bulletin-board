from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from posts.models import Product
from .cart import Cart
from .forms import ProductAddInCartFrom, OrderForm
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.conf import settings
from .models import Order
from django.shortcuts import redirect

def cart(request):
    cart = Cart(request)
    return render(request,'cart/index.html', {'cart':cart})

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = ProductAddInCartFrom(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])

        return HttpResponseRedirect(product.get_absolute_url())

def cart_remove(request, product_id):
    product = get_object_or_404(Product ,pk=product_id)
    cart = Cart(request)
    cart.remove(product)
    return HttpResponseRedirect(reverse('posts:product_detail', args=[product.id]))

@login_required
def send_order(request):
    cart = Cart(request)
    form = OrderForm()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            for order_item in cart:
                order = order_form.save(commit=False)
                order.author = request.user
                order.seller = order_item['product'].author
                order.product = order_item['product']
                order.quantity = order_item['quantity']
                order.total_price = order_item['total_price']
                order.save()
            return redirect('posts:index')
    else:
        return render(request, 'cart/create_order.html', {'cart':cart, 'form':form})

@login_required
def requests_to_order(request):
    if request.user:
        orders = Order.objects.filter(seller=request.user)
    return render(request, 'cart/orders_messages.html', {'orders':orders})