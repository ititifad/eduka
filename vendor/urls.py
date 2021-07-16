from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-vendor/', views.edit_vendor, name='edit_vendor'),
    #path('<int:id>/', views.update_product, name='update_product'),
    #path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),
    path('vendors/', views.vendors, name='vendors'),
    path('<int:vendor_id>/', views.vendor, name='vendor'),
    #path('search/', views.search_vendor, name='search-vendor'),
    #path('vendor/<int:pk>/', views.Vendor_info, name='vendor-info'),
]
