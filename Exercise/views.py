from base64 import urlsafe_b64decode
from email import message
from lib2to3.pgen2.tokenize import generate_tokens
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from Exercise.models import user_details
from WHOLENESS import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from . tokens import generate_token
from formtools.wizard.views import SessionWizardView
from .forms import nameform,genderform,ageform,heightform,weightform,emailform


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
        
        myuser= user_details(first_name=fname,last_name=lname,gender=gender,date_of_birth=dob,height=height,weight=weight,email=email)
        myuser.save()
        return redirect('/signin')
    return render(request,'Exercise/register.html')