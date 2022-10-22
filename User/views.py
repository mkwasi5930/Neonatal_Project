from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login as dj_login
from django.contrib.auth.forms import AuthenticationForm 
from django.shortcuts import HttpResponse
from .forms import NewUserForm

from User.forms import BookForm

# Create your views here.
def HomePage(request):
    context={

    }
    return render(request,'home.html',context)

def BookingPage(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thank')
    else:
        form = BookForm()
    return render(request,'bookappoint.html',{'form': form})

def thankPage(request):
    return HttpResponse("Thanks!! You have booked an Appointment.")

def servicesPage(request):
    context={

    }
    return render(request,'services.html',context)

def contactUsPage(request):
    context={

    }
    return render(request,'contactUs.html',context)

def notification(request):
    context={

    }
    return render(request,'Messages.html',context)

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            dj_login(request,user)
            messages.success(request,'You have successfully registered')
            return redirect('/login')
        messages.error(request,'Invalid details!!Try Again!!')
    form = NewUserForm()
    return render(request,'register.html',{'form' : form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                dj_login(request, user)
                messages.info(request, f"You have logged in as {username}.")
                return redirect('/home')
            else:
                messages.error(request, "Invalid username or password. Try Again!!")
        else:
            messages.error(request,"Invalid username or password. Try Again!!")
    form = AuthenticationForm()
    return render(request,'login.html',{ 'form' : form})

