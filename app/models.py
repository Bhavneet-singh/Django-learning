from django.db import models
from django.utils import timezone

# Create your models here.

class AppNames(models.Model):
    APP_CHOICES =[
        ('F' , 'Finder'), 
        ('M' , 'MAP') , 
        ('C' , 'Call'), 
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'app/')
    price = models.IntegerField(default= 0 )
    time = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length= 2 , choices = APP_CHOICES)
    desciption = models.TextField(default= "" , )

    def __str__(self) :
        return self.name
