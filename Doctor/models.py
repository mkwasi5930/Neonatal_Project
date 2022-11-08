
from email.policy import default
from random import choices
from django.db import models

# Create your models here.

    
class MotherInfor(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length =30)
    nationalId = models.IntegerField(default='12345678')
    email = models.EmailField(max_length=30,default='abedtati1@gmail.com')
    age = models.IntegerField()
    numberOfKids = models.IntegerField(default='1')
    MARITALSTATUS = (
        ('S','Single'),
        ('M','Married'),
    )
    maritalstatus = models.CharField(max_length=30,choices = MARITALSTATUS,default='1')

    def __str__(self) -> str:
        return self.nationalId


    
class Childdetail(models.Model):
    first_Name = models.CharField(max_length=30)
    middle_Name = models.CharField(max_length=30)
    last_Name = models.CharField(max_length=30,null = True)
    mothers_Name= models.CharField(max_length=30)
    fathers_Name = models.CharField(max_length=30,null = True)
    weight = models.CharField(max_length=30)
    height = models.CharField(max_length=30)
    temperature = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    VACCINE_RECEIVED = (
       ('1','Vaccine_1'),
        ('2','Polio 2,Pentavalent $ Rotarix'),
        ('3','Flue Vaccine $ Vitamin A'),
        ('4','Flue Vaccine'),
        ('5','MMR $ Yellow fever'),
        ('6','Menangoccal $ Y conjugate'),
        ('7','Hepatitis A $ Dewormer'),
        ('8','Menangaccal $ MMR')
    )
    vaccine = models.CharField(max_length=30,choices = VACCINE_RECEIVED)

    def __str__(self)->str:
        return self.first_Name

class DoctorInfor(models.Model):
    firstname = models.CharField(max_length = 30,default='moffa')
    lastname = models.CharField(max_length = 30,default='mutuma')
    email = models.EmailField(max_length=30,default='mc123@gmail')

    def __str__(self)->str:
        return self.firstname

class News(models.Model):
    posted_on= models.DateTimeField(auto_now=True)
    about= models.CharField(max_length = 50)
    description = models.TextField(max_length= 10000)