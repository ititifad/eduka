from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=255, help_text="Your business/shop name")
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    is_verified = models.BooleanField(default=False, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name