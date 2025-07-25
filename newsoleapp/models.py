import random
import string
from django.db import models
from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField
from django.utils.text import slugify

# Create your models here.
CATEGORY_CHOICES = ( ('POPULAR', 'Popular Brands'),
             ('NEW', 'New Arrivals'),
             ('SALE', 'Sale Items'),
             ('TRENDING', 'Trending'),
             ('CLASSIC', 'Classic Styles'))

def generate_product_code(length=8): #Generates a random product code
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    categories = MultiSelectField(choices=CATEGORY_CHOICES, default=['POPULAR',])
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    product_code = models.CharField(max_length=20, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.product_code:
            # Generate a unique product code
            code = generate_product_code()
            while Shoe.objects.filter(product_code=code).exists():
                code = generate_product_code()
            self.product_code = code
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

