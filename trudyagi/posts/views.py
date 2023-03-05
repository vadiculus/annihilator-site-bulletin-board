import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormMixin
from .models import Rubric, Product, Product_Image, Review, Category
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, FormView, DeleteView, UpdateView
from .forms import CreateProductForm, CreateReviewForm, FilterProductForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from cart.cart import Cart
from cart.forms import ProductAddInCartFrom
from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from decimal import Decimal
from .attributes_conf import attributes_config

def index(request):
    rubrics = Rubric.objects.all()
    products = Product.objects.all()[:10]
    return render(request, 'posts/index.html', {'rubrics': rubrics,
                                                'products':products})

class CreateProductView(LoginRequiredMixin, CreateView):
    form_class = CreateProductForm
    template_name = 'posts/create-product.html'

    def get_success_url(self):
        return reverse('posts:index')

    def get_context_data(self, **kwargs):
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
    cart_form = ProductAddInCartFrom()
    characteristics = product.characteristics.items()

    if request.method == 'POST':
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            errors = None
            if request.user:
                review = form.save(commit=False)
                review.author = request.user
                review.product = product
                review.save()

        return HttpResponseRedirect(reverse('posts:product_detail', args=[product_unique_id]))

    elif request.method == 'GET':
        rubrics = Rubric.objects.all()
        return render(request, 'posts/detail-product.html', {'rubrics':rubrics,'product':product,
                                                            'review_form': CreateReviewForm,
                                                            'cart_form':cart_form,
                                                             'characteristics':characteristics,})

@csrf_exempt
def search_product_data(request):
    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            search_products = Product.objects.filter(name__icontains=request.POST.get('search_data'))
            if search_products:
                return JsonResponse({'search_data': [prod.name for prod in list(search_products)]})
            else:
                return JsonResponse({'search_data': False})
    else:
        return HttpResponseRedirect(reverse('posts:index'))

def search_product_home(request):
    if bool(request.GET.get('search_name')):
        return HttpResponseRedirect(reverse('posts:search_product_page', args=['list' ,request.GET.get('search_name')]))
    else:
        return redirect('posts:index')

def search_product_page(request, category_slug, product_name):
    search_params_list = {}
    main_category = False
    rubrics = Rubric.objects.prefetch_related('categories').all()
    for attr in request.GET.items():
        if attr[1]:
            search_params_list[attr[0]] = attr[1]
    if category_slug == 'list':
        category = Category.objects.all()
        main_category = 'Все'
        filterForm = FilterProductForm()
    else:
        category = Category.objects.filter(slug=category_slug)
        main_category = category[0].name
        filterForm = FilterProductForm(category_name=main_category.name)
    products = None
    if request.method == 'GET':
        filters = FilterProductForm(request.GET)
        if filters.is_valid():
            price = filters.cleaned_data['price']
            if not price:
                price = False
            if product_name != 'empty':
                products = Product.objects.filter(
                    Q(name__icontains=product_name) &
                    Q(category__in=category))
            else:
                products = Product.objects.filter(
                    Q(category__in=category))
            if search_params_list:
                products = products.filter(Q(attributes=search_params_list))

        else:
            redirect('posts:index')

    return render(request, 'posts/search_product.html', {'rubrics':rubrics,
                                                        'category': main_category,
                                                        'products': products,
                                                        'form': filterForm})

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
            raise PermissionDenied()

class UpdateProductView(UpdateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'posts/update_product.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author == self.request.user:
            return super().get(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    def get_context_data(self, **kwargs):
        kwargs['characteristics'] = self.object.characteristics.items()
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('posts:product_detail', args=[self.get_object().id])

    def form_valid(self, form):
        product = form.save(commit=False)
        product.author = self.request.user
        self.object = product.save()
        for image in self.request.FILES.getlist('images'):
            Product_Image.objects.create(product=product, image=image)
        return HttpResponseRedirect(self.get_success_url())