from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shoes/', views.shoes, name='shoes'),
    path('shoe/<int:shoe_id>/', views.shoe_detail, name='shoe_detail'),
    path('contact/', views.contact, name='contact'),
]