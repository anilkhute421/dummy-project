#from django.contrib import auth
#from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

def index(request):
    return render(request,"index.html")

def sigup(request):
    if request.method=='POST':
        name1=request.POST['t1']
        mobile_no1 = request.POST['t2']
        email1 = request.POST['t3']
        pass1 = request.POST['t4']

        x=User.objects.create_user(username=mobile_no1,first_name=name1,email=email1,password=pass1)
        x.save()
        print("user created")
        return render(request,'login.html')
    else:
        return render(request,'index.html')
# Create your views here.

def login(request):
    return render(request,'logining.html')

def sucess(request):
    if request.method=='POST':
        mob=request.POST['t5']
        pas=request.POST['t6']
        x=auth.authenticate(username=mob,password=pas)
        print("hi")
        if x is not None:
            auth.login(request,x)
            return render(request,'sucess.html')
        else:
            print("not login")
            return render(request,'index.html' )
    else:
        return render(request,'logining.html')
