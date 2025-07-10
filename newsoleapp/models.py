from django.db import models
from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField

# Create your models here.
CATEGORY_CHOICES = ( ('POPULAR', 'Popular Brands'),
             ('NEW', 'New Arrivals'),
             ('SALE', 'Sale Items'),
             ('TRENDING', 'Trending'),
             ('CLASSIC', 'Classic Styles'))

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = MultiSelectField(choices=CATEGORY_CHOICES, default=['POPULAR' ])
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Contact from {self.name} ({self.email})"