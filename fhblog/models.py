from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime
# Create your models here.
class Categories(models.Model):
    cat_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.cat_name
    
    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    # category = models.IntegerField(choices=CUISINE, null=True)
    category = models.CharField(max_length=100, default='other')

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("post-detail", args=(str(self.id)))



    
