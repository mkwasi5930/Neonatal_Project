from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Childdetail, DoctorInfor, MotherInfor

class ContactForm(forms.Form):
    to_email = forms.EmailField(required= True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class childdetailForm(forms.ModelForm):
    class Meta:
        model = Childdetail
        fields = '__all__'

class doctorInforForm(forms.ModelForm):
    class Meta:
        model = DoctorInfor
        fields = '__all__'

class motherInforForm(forms.ModelForm):
    class Meta:
        model = MotherInfor
        fields = '__all__'
    




