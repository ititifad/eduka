from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
import random
from .models import Vendor
from myapp.models import Product

from .forms import ProductForm, VendorForm

def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        vendor_form = VendorForm(request.POST)

        if form.is_valid() and vendor_form.is_valid():
            user = form.save()
            vendor_form = form.save()

            login(request, user)

            vendor = Vendor.objects.create(name=user.username, created_by=user)
            messages.success(request, f'Your account has been successfully created! You can now add your products')
            return redirect('gallery')
        
    else:
        form = UserCreationForm()
        vendor_form = VendorForm()

    return render(request, 'vendor/become_vendor.html', {'form': form,'vendor_form':vendor_form})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.name)
            product.save()
            
            messages.success(request, f'You have successfully added your product')
            return redirect('vendor_admin')
    else:
        form = ProductForm()
    
    return render(request, 'vendor/add_product.html', {'form': form})

@login_required
def edit_vendor(request):
    vendor = request.user.vendor

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        location = request.POST.get('location', '')
        phone_number = request.POST.get('phone_number', '')

        if name:
            vendor.created_by.email = email
            vendor.created_by.save()

            vendor.name = name
            vendor.save()

            return redirect('vendor_admin')
    
    return render(request, 'vendor/edit_vendor.html', {'vendor': vendor})

def vendors(request):
    #vendors = Vendor.objects.all()
    vendors = Vendor.objects.filter(is_verified=True)
    
    return render(request, 'vendor/vendors.html', {'vendors': vendors})
    
def vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    return render(request, 'vendor/vendor.html', {'vendor': vendor})

@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()
    
    return render(request, 'vendor/vendor_admin.html', {'vendor': vendor, 'products': products})

#@login_required
#def update_product(request, id):
    #product = get_object_or_404(Product, id=id)
    #form = ProductForm(instance=product)
     
    #if request.method == 'POST':
        #form = ProductForm(request.POST, request.FILES, instance=product)
        #if form.is_valid():
           # product = form.save(commit=False)
           # product.vendor = request.user.vendor
            #product.slug = slugify(product.name)
            #product.save()
            #return redirect('vendor_admin')
        
    #return render(request, 'vendor/product_update.html', {'form': form})

#@login_required
#def delete_product(request, id):
   # product = get_object_or_404(Product, id=id)

   # if request.method == 'POST':
      #  product.vendor = request.user.vendor
       # product.delete()
       # return redirect('vendor_admin')
        
    #return render(request, 'vendor/delete_product.html', {'product': product})