from distutils.command.upload import upload
from email.policy import default
from operator import mod
from pickle import TRUE
from turtle import position
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Positions(models.Model):
    position = models.CharField(default="MEMBER",max_length=25,unique=True)
    value = models.IntegerField(default=1)

    def __str__(self):
        return self.position

class SocHeads(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    year = models.IntegerField(default=1)
    position = models.ForeignKey(Positions,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='headimages/',null=True,blank=True)

    def __str__(self):
        return self.user.first_name