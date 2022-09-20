from email import message
import imp
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from .models import Vehicle
from django.contrib.auth.models import User,auth


# Create your views here.

def index(request):
    obj=Vehicle.objects.all()
    return render(request,"index.html",{'result':obj})

def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']      
        password=request.POST['password']
        cpassword=request.POST['re_password']
        if password==cpassword:   
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exists")
                return redirect('registration.html') 
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect('registration.html') 
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
            print("User Created");
            return redirect('login.html')
        else:
            messages.info(request,"password not match")
            return redirect('registration.html')
    return render(request, 'registration.html')
    

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('base.html')
        else:
            messages.info(request,"invalid values")
            return redirect('login.html')     
    return render(request,'login.html')

def base(request):
    return render(request,'base.html')    
