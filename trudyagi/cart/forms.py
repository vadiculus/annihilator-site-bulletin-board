from django import forms
from .models import Order

class ProductAddInCartFrom(forms.Form):
    PRODUCT_QUANTITY_CHOICE = [(i,str(i)) for i in range(1,21)]
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICE, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['author', 'seller', 'product', 'quantity', 'total_price', 'read', 'created']
