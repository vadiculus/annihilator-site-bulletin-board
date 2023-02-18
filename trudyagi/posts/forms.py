from django import forms
from .models import Product, Review
from django.utils.text import slugify

class CreateProductForm(forms.ModelForm):
    images = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}))

    class Meta:
        model = Product
        exclude = ('author','slug','rating')

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review','content']
