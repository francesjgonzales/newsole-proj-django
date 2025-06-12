from django.shortcuts import render
from .models import Shoe
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def shoes(request):
    items = Shoe.objects.all()  # Fetch all Shoe objects from the database
    return render(request, 'shoes.html', {"shoes": items})    
def shoe_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)  # Fetch the specific shoe by ID
    return render(request, 'shoe_detail.html', {"shoe": shoe})  
def contact(request):
    return render(request, 'contact.html')