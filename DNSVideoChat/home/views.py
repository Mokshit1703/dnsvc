from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from home.models import Login

# Create your views here.
# I have created  this file - Dhruv

def index(request):
    if request.method == "POST":
        # check if the user has entered correct credentials
        email = request.POST.get('email')
        password = request.POST.get('password')

        # create the user
        login = Login(email=email, password=password)
        login.save()
        messages.success(request, "Your message has been sent!!")
        return redirect('/home')
    return render(request, 'index.html')

def home(request):
     return render(request, 'home.html')

def aboutus(request):
     return render(request, 'about_us.html')

def contact(request):
     if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, address=address, desc=desc, date= datetime.today())
        contact.save()
        return redirect('/contact')
        messages.success(request, "Your message has been sent!!")
        
     return render(request, 'contact_us.html')