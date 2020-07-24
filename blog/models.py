from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length=250)
    def __str__(self):
       return self.blog_title
    pub_date_blog = models.DateTimeField()
    blog_image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date_blog.strftime('%b %e %Y')    
   
   

