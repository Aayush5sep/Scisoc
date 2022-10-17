from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import LatestNews
from user.models import SocHeads

def homepage(request):
    # latest news rendering
    news = LatestNews.objects.all().order_by('date_time')
    # Team Positions rendering
    team = SocHeads.objects.all().order_by('position__value')
    # HomePage Render
    return render(request,'homepage.html',{'news':news,'team':team})