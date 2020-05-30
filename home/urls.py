from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name='home'),
    path('services',views.services, name='services'),
    path('we',views.about, name='we'),
    path('gallery',views.gallery, name='gallery'),
    path('contact',views.contact, name='contact'),
    path('apply',views.apply, name='apply'),
    path('social',views.bb, name='social'),
    path('get',views.get, name='get'),
]    