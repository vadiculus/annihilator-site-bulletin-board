from django import forms
from .models import Product, Review
from django.utils.text import slugify

class CreateProductForm(forms.ModelForm):
    images = forms.FileField(required=False, widget=forms.FileInput(attrs={'id':'images_input', 'multiple': True}))

    class Meta:
        model = Product
        exclude = ('author','slug','rating')
        widgets = {
            'image': forms.FileInput(attrs={'id': 'image_input'})
        }

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review','content']
