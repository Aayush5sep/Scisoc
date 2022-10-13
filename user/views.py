from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def loginpage(request):
    return render(request,'user/login.html')

def signuppage(request):
    return render(request,'user/signup.html')

def signupuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cfpassword=request.POST['cfpassword']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']

        if password != cfpassword:
            messages.error(request,"Passwords do not match")
            return redirect("/user/signuppage")

        newuser = User.objects.create_user(username,email,password)
        newuser.first_name=fname
        newuser.last_name=lname
        newuser.save()
        user=authenticate(username=username,password=password)
        login(request,user)
        messages.success(request,"User Account Created Successfully")
        return render(request,'')
    else:
        return HttpResponse("Creating new user account failed !")

def loginuser(request):
    if request.method=='POST':
        login_username=request.POST['username']
        login_password=request.POST['password']

        user=authenticate(username=login_username,password=login_password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successful')
            return redirect("/")
        else:
            messages.error(request,'Login Failed')
            return HttpResponse("Oops! Login Failed")
    else:
        return HttpResponse("Unsecured Login Error !!")

def logoutuser(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return redirect("/")