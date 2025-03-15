from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from .models import *
from Appointment_app.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url ="pandit_signup")
def pandit_profile_view(request,id):
    obj = Pandit.objects.get(Pandit_Id = id)
    print(obj.Name)
    print(obj.Image)
    obj2 = Appointment_Table.objects.filter(Pandit_Id = id)
    print(obj2)
    return render(request,"Pandit_app/profile.html",{"Data":obj,"data1":obj2}) 

def pandit_signup_view(request):
    if(request.method == "POST"):
        print(request.POST,request.FILES)
        id = request.POST.get("id")
        nm = request.POST.get("name")
        ag = request.POST.get("age")
        area = request.POST.get("area")
        exp = request.POST.get("experience")
        pht = request.FILES.get("photo")
        eml = request.POST.get("eml")
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        print(id,nm,ag,area,exp,pht,eml,uname,pwd)
        if(User.objects.filter(username=uname).exists()): 
            print("User already exists.")
            messages.error(request,"Username already taken. Please Choose another")
            return render(request,"Pandit_app/pandit_signup.html",{'error':'Username already exist'})
        else:
            User.objects.create_user(username=uname,email=eml,password=pwd)
            obj = Pandit(Pandit_Id=id,Name=nm,Age=ag,Area=area,Work_Experience=exp,Image=pht,Email_Id=eml,Username=uname,Password=pwd)
            obj.save()
            print("User created successfully")
            return redirect("pandit_signin")

    return render(request,"Pandit_app/pandit_signup.html")


def pandit_signin_view(request):
    if(request.method=="POST"):
        print(request.POST)
        id = request.POST.get("id")
        un = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        try:
            obj = Pandit.objects.get(Pandit_Id=id)
            if (obj.Username==un and obj.Password == pwd):
                user = authenticate(request,username=un,password=pwd)
                if user is not None:
                    login(request,user)
                    return redirect("pandit_profile",id)
                else:
                    messages.error(request,"Invalid credentials")
        except Pandit.DoesNotExist:
            messages.error(request,"Pandit ID not found")

    return render(request,"Pandit_app/pandit_signin.html")


def pandit_signout_view(request):
    logout(request)
    return redirect("pandit_signin")

@login_required(login_url ="pandit_signup")
def appointment_confirmation_view(request,id):
    obj = Appointment_Table.objects.get(id = id)
    pid = obj.Pandit_Id.Pandit_Id
    obj.Status = "Confirmed"
    obj.save()
    print(pid)
    return redirect("pandit_profile",id = pid)

@login_required(login_url ="pandit_signup")
def appointment_declined_view(request,id):
    obj = Appointment_Table.objects.get(id = id)
    pid = obj.Pandit_Id.Pandit_Id
    obj.Status = "Declined"
    obj.save()
    print(pid)
    return redirect("pandit_profile",id = pid)


def main_home_view(request):
    return render(request,"Pandit_app/main_home.html")


 



