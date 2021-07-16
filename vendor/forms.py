from django import forms
from django.forms import ModelForm
from .models import Vendor
from myapp.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'name', 'description', 'price', 'state', 'is_featured']

class VendorForm(forms.ModelForm):
    
    class Meta:
        model = Vendor
        fields = ['name', 'phone_number', 'location', 'description']