from django.shortcuts import render, redirect
from .models import Property

# Create your views here.

# GET

def home(request):
    return render(request, 'index.html')

def properties(request):
    context = {
    'allP': Property.objects.all()
    }
    return render(request, 'properties.html', context)

#POST

def addProperty(request):
    Property.objects.create(
        address = request.POST['address'],
        postcode = request.POST['postcode'],
        town = request.POST['town'],
        pic = request.FILES['pic']
    )
    return redirect('/properties')