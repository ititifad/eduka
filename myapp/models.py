from django.db import models
from vendor.models import Vendor
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=255, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def get_absolute_url(self):
        return reverse('product_list_by_category',
                       args=[self.slug])

class Product(models.Model):
    
    STATE = (
        ('new', 'New'),
        ('used', 'Used'),
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    state = models.CharField(max_length=20, choices=STATE, default='New')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.id, self.slug])