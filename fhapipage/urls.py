from django.urls import path, include
from . import views

#URLS.PY FHAPIPAGE
urlpatterns = [
    path('apirapid/', views.apiRapid, name='apirapid'),
]