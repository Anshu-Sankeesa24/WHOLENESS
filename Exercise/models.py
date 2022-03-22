from calendar import Calendar, calendar
from datetime import date
from email.message import EmailMessage
import turtle
from django.db import models
from django.contrib.auth.models import User,AbstractUser




class profile(models.Model):
    name=models.CharField(max_length=100,null=True)
    dob=models.DateField(blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    gender =models.CharField(blank=True,null=True,max_length=100)
    height=models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=5)
    weight =models.DecimalField(decimal_places=2,max_digits=5,null=True)
    #user=models.OneToOneField(User, on_delete=models.CASCADE)
    #auth_token=models.CharField(max_length=100)
    is_verified =models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    

