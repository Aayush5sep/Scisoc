from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
# Create your views here.

def contactpage(request):
    return render(request,'')

def addissue(request):
    name=request.GET['name']
    email=request.GET['email']
    issue=request.GET['issue']
    prob=Contact(name=name,email=email,issue=issue)
    prob.save()
    if prob is not None:
        messages.success(request,"Contact Request/Issue Submiited. We will reply as soon as possible.")
    return redirect('about/contactpage/')