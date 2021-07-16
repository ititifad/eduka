from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from vendor.models import Vendor
from cart.forms import CartAddProductForm
# Create your views here.

#def gallery(request):
    #category = request.GET.get('category')
    #if category == None:
        #products = Product.objects.all()
    #else:
        #products = Product.objects.filter(category__name=category)

    #categories = Category.objects.all()
    #context = {'categories': categories, 'products': products}
    #return render(request, 'myapp/gallery.html', context)

#def viewProduct(request, pk):
    #product = Product.objects.get(id=pk)
    #return render(request, 'myapp/product.html', {'product': product})

def gallery(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_featured=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'myapp/gallery.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                is_featured=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'myapp/product.html',
                  {'product': product,
                   'cart_product_form': cart_product_form
                   })

def addProduct(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            product = Product.objects.create(
                name=data['name'],
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'myapp/add.html', context)

def callback(request):
    return render(request, 'myapp/callback.html')