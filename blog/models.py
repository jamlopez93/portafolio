from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length=250)
    pub_date_blog = models.DateTimeField()
    blog_image = models.ImageField(upload_to='images/')
    body = models.TextField()

