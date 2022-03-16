from django.db import models

# Create your models here.

class name(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)

    def __str__(self):
        return self.fname,self.lname

class gender(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.sex

class dob(models.Model):
    date_of_birth=models.DateField(max_length=100)

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