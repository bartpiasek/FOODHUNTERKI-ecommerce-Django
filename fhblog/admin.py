from django.contrib import admin
from .models import Post, Categories, UserProfile

# Register your models here.
admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(UserProfile)

