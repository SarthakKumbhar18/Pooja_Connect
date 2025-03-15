from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login,logout,authenticate
from Appointment_app.models import *
from django.contrib.auth.decorators import login_required
from Pandit_app.models import *
# Create your views here.
def user_signup_view(request):
    if(request.method == "POST"):
        print(request.POST)
        uid = request.POST.get("uid")
        nm = request.POST.get("name")
        eml = request.POST.get("emlid")
        unm = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        print(uid,nm,eml,unm,pwd)
        if(User.objects.filter(username=unm).exists()):
            print("User already exists.")
            messages.error(request,"Username already taken. Please Choose another")
            return render(request,"Pandit_app/pandit_signup.html",{'error':'Username already exist'})
        else:
            User.objects.create_user(username=unm,email=eml,password=pwd)
            obj = User_table(User_Id = uid,Name = nm,Email_Id = eml,Username = unm,Password = pwd)
            obj.save()
            print("User created successfully")
            return redirect("user_signin")

    return render(request,"user_app/usersignup.html")

def user_signin_view(request):
    if(request.method=="POST"):
        print(request.POST)
        uid = request.POST.get("uid")
        unm = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        try:
            obj = User_table.objects.get(User_Id=uid)
            if (obj.Username==unm and obj.Password == pwd):
                user = authenticate(request,username=unm,password=pwd)
                if user is not None:
                    login(request,user)
                    return redirect("user_homepage",id=uid)
                else:
                    messages.error(request,"Invalid credentials")
        except Pandit.DoesNotExist:
            messages.error(request,"Pandit ID not found")

    return render(request,"user_app/usersignin.html")

@login_required(login_url="user_signin")
def user_homepage_view(request,id):
    print(id)
    objs = Pandit.objects.all()
    return render(request,"user_app/user_home.html",{"pandits":objs,"uid":id})

@login_required(login_url="user_signin")
def appointment_booking(request):
    if(request.method == "POST"):
        print(request.POST)
        pid = request.POST.get("pid")
        uid = request.POST.get("uid")
        nm = request.POST.get("name")
        phn = request.POST.get("phn")
        dt = request.POST.get("date")
        wk = request.POST.get("work")
        print(pid,uid,nm,phn,dt,wk)
        user_instance = User_table.objects.get(User_Id=uid) 
        pandit_instance = Pandit.objects.get(Pandit_Id=pid)
        obj = Appointment_Table(User_ID = user_instance,Pandit_Id = pandit_instance,Name = nm,Phone_no = phn, Date = dt,Work = wk)
        obj.save()
        return redirect("user_appointment_table", id=uid)
    return render(request, "user_app/appointment.html")

@login_required(login_url="user_signin")
def user_appointment_table_view(request,id):
    uid = id 
    obj = Appointment_Table.objects.filter(User_ID=id)
    print(obj)
    return render(request,"user_app/appointment_table.html",{"Data":obj,"uid":uid}) 

@login_required(login_url="user_signin")
def update_appointment_view(request,id):
    if(request.method == "POST"):
        print(request.POST)
        pid = request.POST.get("pid")
        uid = request.POST.get("uid")
        nm = request.POST.get("name")
        pn = request.POST.get("phn")
        dt = request.POST.get("date")
        wk = request.POST.get("work")
        user_instance = User_table.objects.get(User_Id=uid) 
        pandit_instance = Pandit.objects.get(Pandit_Id=pid)
        obj = Appointment_Table.objects.get(id = id)
        obj.Pandit_Id = pandit_instance
        obj.User_ID = user_instance
        obj.Name = nm
        obj.Phone_no = pn
        obj.Date = dt
        obj.Work = wk
        obj.Status = "Pending"
        obj.save()

        obj1 = Appointment_Table.objects.filter(User_ID=uid)
        print(obj1)
        return render(request,"user_app/appointment_table.html",{"Data":obj1,"uid":uid})


    obj = Appointment_Table.objects.get(id = id)
    print(obj)
    return render(request,"user_app/update_appointment.html",{"objs":obj})

@login_required(login_url="user_signin")
def delete_appointment_view(request, id):
    obj = get_object_or_404(Appointment_Table, id=id)  
    uid = obj.User_ID.User_Id  
    obj.delete()  
    remaining_appointments = Appointment_Table.objects.filter(User_ID=uid)  
    
    return render(request, "user_app/appointment_table.html", {"Data": remaining_appointments,"uid":uid})


def user_signout_view(request):
    logout(request)
    return redirect("main_home")



 
# Make panditji able to change status or delete appointment





