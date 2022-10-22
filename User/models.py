from django.db import models

# Create your models here.
class Book(models.Model):
    first_Name= models.CharField(max_length=30)
    last_Name= models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    date_created= models.DateTimeField(auto_now=True)
    phone_No= models.IntegerField()
    your_Area=models.CharField(max_length=30)
    text = models.TextField(max_length=100)

    def __str__(self) -> str:
        return self.email