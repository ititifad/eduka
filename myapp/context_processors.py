from .models import Category

def categories(request):
    category = Category.objects.all()
    return {'categories': category}