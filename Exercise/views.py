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

class signup(SessionWizardView):
    template_name='Exercise/msf.html'
    form_list= [nameform,genderform,ageform,heightform,weightform,emailform]

    form_name=nameform()
    if form_name.is_valid():
        form_name.save()



    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]

        return render(self.request, 'Exercise/signin.html', {'form': form_data})

def signin(request):
    
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

def signup1(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,"username already exist")
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request,"Email already exist")
            return redirect('signup')
        
        if len(username)>10:
            messages.error(request,"keep length of the username less than")
            return redirect('signup')
        
        if len(username)<5:
            messages.error(request,"username is too short")
            return redirect('signup')

        if pass1!=pass2:
            messages.error(request,"passwords are different")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request,"username must be mix of numbers and alphabets")
            return redirect('signup')

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.is_active =False

        myuser.save()

        messages.success(request,"your accout has been created successfully. we have sent an email please confirm it")

        #WELCOME TO EMAIL

        subject='email conformation'
        message='hello'+myuser.first_name +"!! \n\n welcome to wholeness \n thank you for visitng our website \nplease conform your email address in order to activate your account.\n thanking you"

        from_email=settings.EMAIL_HOST_USER
        to_list=[myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        
        current_site=get_current_site(request)
        
        email_subject="confirm your email !!"
        message2=render_to_string('email_conformation.html',{
            'name':myuser.first_name,
            'domain':current_site.domain,
            'uid': urlsafe_base64_decode(force_bytes(myuser.pk)),
            'token':generate_token.make_token(myuser)

        })
        email=message.EmailMessage(email_subject,message2,settings.EMAIL_HOST_USER,[myuser.email])


        return redirect('signin')

    return render(request,"Exercise/namepage.html")


def logout(request):
    logout(request)
    messages.success(request,"Logged out Successfully!")
    return redirect('index')

'''def activate(request, uidb64,token):
    try:
        #uid =force_text(urlsafe_base64_decode(uidb64))
        myuser=User.onjects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser=None
    
    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active=True
        myuser.save()
        login(request,myuser)
        return redirect('home')
    else:
        render(request, 'activation_failed.html')'''