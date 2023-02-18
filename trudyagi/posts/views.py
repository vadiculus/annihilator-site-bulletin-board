import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormMixin

from .models import Rubric, Product, Product_Image, Review
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, FormView, DeleteView, UpdateView
from .forms import CreateProductForm, CreateReviewForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from cart.cart import Cart
from cart.forms import ProductAddInCartFrom
from django.contrib import messages
from django.shortcuts import redirect

def index(request):
    rubrics = Rubric.objects.all()
    products = Product.objects.all()[:10]
    return render(request, 'posts/index.html', {'rubrics': rubrics,
                                                'products':products})

class CreateProductView(CreateView):
    form_class = CreateProductForm
    template_name = 'posts/create-product.html'

    def get_success_url(self):
        return reverse('posts:index')

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

    def form_valid(self, form):
        product = form.save(commit=False)
        product.author = self.request.user
        self.object = product.save()
        for image in self.request.FILES.getlist('images'):
            Product_Image.objects.create(product=product, image=image)
        return HttpResponseRedirect(self.get_success_url())

def get_by_rubric(request, rubric_slug):
    rubrics = Rubric.objects.all()
    rubric = Rubric.objects.get(slug=rubric_slug)
    products = Product.objects.filter(category__rubric=rubric)
    return render(request, 'posts/by_rubric.html', {'rubric':rubric,'rubrics':rubrics,'products': products})

def product(request, product_unique_id):
    product = get_object_or_404(Product.objects.prefetch_related('reviews' ,'reviews__author'), pk=product_unique_id)

    #Product.objects.prefetch_related('reviews' ,'reviews__author').get(slug=product_slug)

    cart_form = ProductAddInCartFrom()
    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = CreateReviewForm(request.POST)
            print(request.POST)
            if form.is_valid():
                errors = None
                if request.user:
                    review = form.save(commit=False)
                    review.author = request.user
                    review.product = product
                    review.save()
            return JsonResponse({'action':'success_review_form'})
    elif request.method == 'GET':
        rubrics = Rubric.objects.all()
        return render(request, 'posts/detail-product.html', {'rubrics':rubrics,'product':product,
                                                            'review_form': CreateReviewForm,
                                                            'cart_form':cart_form})

@csrf_exempt
def search_product_data(request):
    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            search_products = Product.objects.filter(name__icontains=request.POST.get('search_data'))
            if search_products:
                return JsonResponse({'search_data': [(prod.name, prod.get_absolute_url()) for prod in list(search_products)]})
            else:
                return JsonResponse({'search_data': False})
    else:
        return HttpResponseRedirect(reverse('posts:index'))

def search_product(request, product_name):
    products = Product.objects.filter(name__icontains=request.POST.get('search_data'))
    rubrics = Rubric.objects.all()
    return render(request, 'posts/index.html', {'rubrics': rubrics,
                                                'products': products})

@csrf_exempt
def delete_review(request, review_id):
    review = Review.objects.select_related('author').get(pk=review_id)
    if review.author == request.user:
        review.delete()
        return JsonResponse({'action':'success_deleted'})

class DeleteProductView(DeleteView):
    model = Product
    success_url = reverse_lazy('posts:index')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author == self.request.user:
            return super().get()
        else:
            return redirect('posts:index')

class UpdateProductView(UpdateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'posts/update_product.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author == self.request.user:
            return super().get()
        else:
            return redirect('posts:index')

    def get_success_url(self):
        return reverse('posts:product_detail', args=[self.get_object().id])

    def form_valid(self, form):
        product = form.save(commit=False)
        product.author = self.request.user
        self.object = product.save()
        for image in self.request.FILES.getlist('images'):
            Product_Image.objects.create(product=product, image=image)
        return HttpResponseRedirect(self.get_success_url())