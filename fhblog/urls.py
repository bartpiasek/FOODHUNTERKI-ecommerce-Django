from django.urls import path
#from .views import apiRapid
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]

