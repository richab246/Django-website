from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
  context = {
     'variable': "Richa is great"
  }
  return render(request, 'index.html', context)

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