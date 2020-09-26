from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime


# Create your views here.
# I have created  this file - Dhruv

def index(request):
    return render(request, 'index.html')

def home(request):
     return render(request, 'home.html')

def aboutus(request):
     return render(request, 'about_us.html')

def contact(request):
     return render(request, 'contact_us.html')