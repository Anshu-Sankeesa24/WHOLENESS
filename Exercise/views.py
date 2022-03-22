from base64 import urlsafe_b64decode
from email import message
import email
from lib2to3.pgen2.tokenize import generate_tokens
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from Exercise.models import profile
from WHOLENESS import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from . tokens import generate_token
from formtools.wizard.views import SessionWizardView
import uuid
from .models import profile
from django.conf import settings


# Create your views here.
def index(request):
    return render(request,"Exercise/index.html")

def register(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        gender=request.POST['gender']
        dob=request.POST['dob']
        height=request.POST['height']
        weight=request.POST['weight']
        
        send_mail_verify(email)
        user_obj=profile(name=fname+" "+lname,gender=gender,dob=dob,height=height,weight=weight,email=email)
        user_obj.save()
       
        messages.success(request,"your details had been stored succesfully")
        #return redirect('/login')
        
        messages.success(request,"something occured please try again")
            #return redirect('index')
        
    return render(request,'Exercise/register.html')
    

def send_mail_verify(email):
    subject ="you account nees to be verified"
    message =f'hii \nclick the link to verify '
    email_from =settings.EMAIL_HOST_USER
    recipent_list=[email]
    send_mail(subject,message,email_from,recipent_list)

def login(request):
    
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        #return redirect('home')

        user=authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"Exercise/home.html", {'fname':fname})
        else:
            messages.error(request,"Invalid Credtials")
            return redirect('signin')

    return render(request,"Exercise/login.html")



def logout(request):
    logout(request)
    messages.success(request,"Logged out Successfully!")
    return redirect('index')
