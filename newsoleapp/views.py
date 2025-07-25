from django.shortcuts import render

from newsoleapp.forms import ContactForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


from .models import ContactForm, Shoe
# Create your views here.
def index(request):
    latest = Shoe.objects.filter(categories='POPULAR')  # Fetch the specific shoe by ID
    return render(request, 'index.html', {"shoes": latest})
def about(request):
    return render(request, 'about.html')
def shoes(request):
    items = Shoe.objects.all()  # Fetch all Shoe objects from the database
    return render(request, 'shoes.html', {"shoes": items})    
""" def shoe_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)  # Fetch the specific shoe by ID
    return render(request, 'shoe_detail.html', {"shoe": shoe})   """
def shoe_slug(request, slug):
    shoe = Shoe.objects.get(slug=slug)  # Fetch the specific shoe by slug
    return render(request, 'shoe_detail.html', {"shoe": shoe})  

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import ContactForm



@csrf_protect
def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect(reverse('index'))
        else:
            # Return the form with errors and user input preserved
            return render(request, 'contact_form.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'contact_form.html', {'form': form})
        
        