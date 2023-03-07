from django import forms
from .models import Product, Review
from django.utils.text import slugify
from .attributes_conf import attributes_config

class CreateProductForm(forms.ModelForm):
    price = forms.DecimalField(label='Цена',max_digits=8, decimal_places=2 ,required=False)
    images = forms.FileField(required=False, widget=forms.FileInput(attrs={'id':'images_input', 'multiple': True}))

    class Meta:
        model = Product
        exclude = ('author','slug','rating')
        widgets = {
            'image': forms.FileInput(attrs={'id': 'image_input'}),
            'price': forms.NumberInput(),
            'characteristics': forms.HiddenInput(),
        }

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review','content']
        validators = []

class FilterProductForm(forms.Form):
    price = forms.DecimalField(required=False)
    def __init__(self, *args, **kwargs):
        category_attrs = attributes_config.get(kwargs.get('category_name','list'), {})
        print(category_attrs)
        if kwargs.get('category_name'):
            del kwargs['category_name']
        super(FilterProductForm, self).__init__(*args, **kwargs)
        for attr in category_attrs.items():
            self.fields[attr[0]] = attr[1]

    class Meta:
        fields = '__all__'

