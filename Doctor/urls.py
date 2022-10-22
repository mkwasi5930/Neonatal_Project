from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name ='home'),
    path('mothersPage',views.mothersPage,name = 'mothersPage'),
    path("success", views.successView, name="success"),
    path('details',views.childdetailPage,name='details'),
    path('doctorInfor',views.doctorInforPage,name='doctorInfor'),
    path('motherInfor',views.motherInforPage,name='motherInfor'),
    path('thanks',views.thanksPage,name='thanks'),
    path('notifications',views.notifications,name='notifications'),
    path('logout',views.logoutPage,name='logout'),
    

]