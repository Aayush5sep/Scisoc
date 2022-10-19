from email.policy import default
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    email=models.EmailField(null=False,blank=False)
    issue=models.TextField(max_length=1000)
    dtime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    event=models.CharField(max_length=50,blank=True,null=True)
    image=models.ImageField(upload_to='gallery/')
    slideshow=models.BooleanField(default=False)

    def __str__(self):
        return self.event