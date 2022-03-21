from calendar import Calendar, calendar
from django.db import models

# Create your models here.

class name(models.Model):
    f_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    def __str__(self):
        return self.fname,self.lname

class gender(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T','others'),
    )
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.sex

class dob(models.Model):
    date_of_birth=models.DateField(blank=True, null=True)

    def __str__(self):
        return self.date_of_birth

class height(models.Model):
    height =models.CharField(max_length=100)
    
    def __str__(self):
        return self.height

class weight(models.Model):
    weight =models.CharField(max_length=100)
    
    def __str__(self):
        return self.weight

class email(models.Model):
    email=models.EmailField(max_length=100)

    def __str__(self):
        return self.email

class user_details(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T','others'),
    )
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth=models.DateField(blank=True, null=True)
    height=models.DecimalField(max_digits=6,decimal_places=2)
    weight=models.DecimalField(max_digits=6,decimal_places=2)
    email=models.EmailField(max_length=100)
    objects=models.Manager()