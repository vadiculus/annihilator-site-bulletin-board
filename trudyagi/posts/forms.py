from django import forms
from django.forms.renderers import get_default_renderer
from django.forms.utils import ErrorList
from django.utils.datastructures import MultiValueDict

from .models import Product, Review
from django.utils.text import slugify
from .attributes_conf import attributes_config
import copy
from django.utils.translation import gettext as _

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
    review = forms.IntegerField(label='Оценка',max_value=5, widget=forms.NumberInput())
    class Meta:
        model = Review
        fields = ['review','content']

class FilterProductForm(forms.Form):
    PRODUCT_CONDITION_CHOICE = (
        ('n', 'Новый'),
        ('u', 'Б/у'),
    )
    SALE_TYPE_CHOICE = (
        ('s', 'Продажа'),
        ('e', 'Обмен'),
        ('f', 'Даром')
    )
    max_price = forms.IntegerField(required=False, max_value=99999999)
    min_price = forms.IntegerField(required=False, min_value=0)
    condition = forms.MultipleChoiceField(required=False,choices=PRODUCT_CONDITION_CHOICE, widget=forms.CheckboxSelectMultiple)
    sale_type = forms.MultipleChoiceField(required=False,choices=SALE_TYPE_CHOICE, widget=forms.CheckboxSelectMultiple)
    def __init__(self, category_name=None, *args, **kwargs):
        category_attrs = attributes_config.get(kwargs.get('category_name','list'), {})
        if kwargs.get('category_name'):
            del kwargs['category_name']
        super(FilterProductForm, self).__init__(*args, **kwargs)
        for name, value in category_attrs.items():
            self.fields[name] = value

    class Meta:
        fields = '__all__'

