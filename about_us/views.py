from django.shortcuts import render ,render_to_response

# Create your views here.


def about(request):
    return render('about/about.html')