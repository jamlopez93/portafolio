from django.db import models

# Create your models here.

class blogpost(models.Model):
    blog_title = models.CharField(max_length=50)
    pub_date_blog = models.CharField(max_length=30)
    blog_image = models.ImageField(upload_to='images/')
    body = models.CharField(max_length=500)

