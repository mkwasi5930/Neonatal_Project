from django.urls import path
from . import views


urlpatterns= [
    path('',views.HomePage,name= 'Home'),
    path('book',views.BookingPage,name='book'),
    path('thank',views.thankPage,name='thank'),
    path('services',views.servicesPage,name='services'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('contactUs',views.contactUsPage,name='contactUs'),
    path('messages',views.notification,name='messages'),
]