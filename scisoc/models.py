from django.db import models

# latest news model
class LatestNews(models.Model):
    title = models.CharField(max_length=200,null=False)
    text = models.TextField(null=True,blank=True)
    link = models.URLField(null=True,blank=True)
    file = models.FileField(upload_to='news/',null=True,blank=True)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Latest News'
        verbose_name_plural='Latest News'

    def __str__(self):
        return self.title