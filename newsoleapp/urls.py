from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shoes/', views.shoes, name='shoes'),
    path('shoe/<slug:slug>/', views.shoe_slug, name='shoe_slug'),
    path('contact/', views.contact_form, name='contact_form'),
]

