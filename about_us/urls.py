
from django.urls import path
from .import views 
# from m=contact_us/views.py import contactView ,successView


urlpatterns = [
    path(r'about/',views.about,name='about'),


    
] 
