from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Categories(models.Model):
    cat_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.cat_name
    
    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post_thumbnail_image = models.ImageField(upload_to='images/fhblog', max_length=None, null=True, blank=True)
    category = models.CharField(max_length=100, default='other')
    snippet = models.CharField(max_length=100, default='snippet')

    def __str__(self):
        return str(self.title) + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("post-detail", args=(str(self.id)))


#USER MODEL (BIO, IMG ETC.) - with OneToOne django auth user
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300)
    profilepicture = models.ImageField(upload_to='images/fhblog/profiles', max_length=None, null=True, blank=True)
    instalink = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    #ERROR PIC, GET ATTR STRING, BUT PIC IS IMAGEFIELD
