
from django.urls import path
from .import views 
# from m=contact_us/views.py import contactView ,successView


urlpatterns = [
    path('contact/',views.contactView,name='contact'),
    path('success/',views.successView,name='success')


    
] 
