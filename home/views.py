from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def courses(request):
  return render(request, 'courses.html')

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

def handleSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email1 = request.POST['email1']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for errorneous inputs
        if len(username) > 10:
          messages.error(request, "Username must be under 10 characters")
          return redirect('home')
        if not username.isalnum():
          messages.error(request, "Username should contain only letter and alphabets")
          return redirect('home')
        if pass1 != pass2:
          messages.error(request, "Passwords do not match")
          return redirect('home')

        # Create the User
        myuser = User.objects.create_user(username, email1, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account is successfully created")
        return redirect("home")
    else:
      return HttpResponse("404 - Not Found")

def handleLogin(request):
  if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
           login(request, user)
           messages.success(request, "Successfully Logged In")
           return redirect("home")
        else:
          messages.error(request, "Invalid Credentials, Please try again")
          return redirect("home")
  return HttpResponse('404 - Not Found')

def handleLogout(request):
  logout(request)
  messages.success(request, "Successfully Logged Out")
  return redirect("home")
