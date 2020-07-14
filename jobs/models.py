from django.db import models

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

class blogpost(models.Model):
    blog_title = models.CharField(max_length=50)
    pub_date_blog = models.CharField(max_length=30)
    blog_image = models.ImageField(upload_to='images/')
    body = models.CharField(max_length=500)




