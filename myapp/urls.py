from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<slug:category_slug>/', views.gallery,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
    path('add/', views.addProduct, name='add'),
    path('callback/', views.callback, name='callback')
]
