from django.urls import path
from . import views


urlpatterns = [
    path('', views.email_sender, name='email_sender')
    ]