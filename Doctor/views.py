from django.shortcuts import render,HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail,BadHeaderError
from django .conf import settings
from User .models import Book

from Doctor.forms import ContactForm, childdetailForm, doctorInforForm, motherInforForm
from .models import*
# Create your views here.

def home(request):
    context ={}
    return render(request,"index.html",context)



def notifications(request):
    book = Book.objects.all()
    context = {
        'books':book
    }
    return render(request,'notification.html',context)



def mothersPage(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            to_email = form.cleaned_data["to_email"]
            message = form.cleaned_data['message']
            if subject and message and to_email:
                try:
                    send_mail(subject, message,[settings.EMAIL_HOST_USER],[to_email] )
                except BadHeaderError:
                    return HttpResponse("Invalid header found.")
                return redirect("success")
            return HttpResponse("Make sure all fields are entered and valid.")    
    return render(request, 'page.html', {"form": form})

def successView(request):
    return HttpResponse("Success! Thank you for your message.")

def childdetailPage(request):
    if request.method == 'POST':
        form = childdetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/doctorInfor')
    else:
      form = childdetailForm()
    return render(request, 'childdetail.html', {'form': form})

def doctorInforPage(request):
    if request.method == 'POST':
        form = doctorInforForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/motherInfor')
    else:
      form = doctorInforForm()
    return render(request, 'doctorInfor.html', {'form': form})

def motherInforPage(request):
    if request.method == 'POST':
        form = motherInforForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thanks')
    else:
      form = motherInforForm()
    return render(request, 'motherInfor.html', {'form': form})

def thanksPage(request):
    return HttpResponse("Thanks received.")

def logoutPage(request):
    return redirect('/login')



