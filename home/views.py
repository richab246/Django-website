from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def products(request):
  return render(request, 'products.html')

def contact(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    contact = Contact(name=name, email=email, phone=phone, password=password, date=datetime.today())
    contact.save()
    messages.success(request, 'Your message is sent!')
  return render(request, 'contact.html')

def loginUser(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    # check if user has entered correct credentials
    user = authenticate(username=username, password=password)
    if user is not None:
       # A backend authenticated the credentials 
       login(request, user)
       return redirect("/")
    else:
       # No backend authenticated the credentials
       return render(request, 'login.html')

  return render(request, 'login.html')

def logoutUser(request):
  logout(request)
  return redirect("/login")
