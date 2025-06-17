from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tags = [ ('POPULAR', 'Popular Brands'),
             ('NEW', 'New Arrivals'),
             ('SALE', 'Sale Items'),
             ('TRENDING', 'Trending'),
             ('CLASSIC', 'Classic Styles')]
    category = models.CharField(max_length=20, choices=tags, default='POPULAR')

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Contact from {self.name} ({self.email})"