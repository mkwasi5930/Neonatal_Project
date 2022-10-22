from django.contrib import admin

from Doctor.models import DoctorInfor, Childdetail, MotherInfor

# Register your models here.
admin.site.register(Childdetail)
admin.site.register(DoctorInfor)
admin.site.register(MotherInfor)