from django.urls import path, include
# from .views import views
# from .views import apiRapid
from .views import apiRapid
from . import views

#URLS.PY FHAPIPAGE
urlpatterns = [
    path('', views.apiRapid, name='apirapid')
    # path('apirapid/', views.recipeapi, name='apirapid'),
]