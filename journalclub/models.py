from django.db import models

# Create your models here.

class event(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=500,blank=True,null=True)
    priority=models.IntegerField(default=0)
    def __str__(self):
        return self.id

class twcaos(models.Model):
    event=models.ForeignKey(event,on_delete=models.CASCADE)
    title=models.CharField(max_length=40)
    ytlink=models.URLField(null=False,blank=False)
    priority=models.IntegerField(default=0)
    def __str__(self):
        return self.title

class fryums(models.Model):
    title=models.CharField(max_length=100)
    images=models.ImageField(upload_to='journal/fryums/',null=False,blank=False)
    desc=models.TextField(null=True,blank=True)
    link=models.URLField(null=True,blank=True)
    importance=models.IntegerField(default=0)
    def __str__(self):
        return self.title

class content(models.Model):
    event=models.ForeignKey(event,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='journal/content/')
    desc=models.TextField()
    link=models.URLField()
    importance=models.IntegerField(default=0)
    def __str__(self):
        return self.title