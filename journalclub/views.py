from django.shortcuts import render
from .models import event,twcaos,fryums,content

# Create your views here.

def mainpage(request):
    fryms=fryums.objects.all().order_by('-importance')
    events=event.objects.all()
    twcas={}
    for evnt in events:
        season=twcaos.objects.all().filter(event=evnt).order_by('-priority')
        twcas[evnt.title]=season
    allevents={}
    for evnt in events:
        comp=content.objects.all().filter(event=event).order_by('-importance')
        allevents[evnt.title]=comp
    params={'fryums':fryms,'twcaos':twcas,'events':allevents}
    return render(request,'journals/mainpage.html',params)