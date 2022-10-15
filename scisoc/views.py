from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import LatestNews

def homepage(request):
    # latest news rendering
    news=LatestNews.objects.all().order_by('date_time')
    # HomePage Render
    return render(request,'homepage.html',{'news':news})