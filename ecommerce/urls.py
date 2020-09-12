"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fhstore.urls')),
    path('api/', include('fhapipage.urls')),
    path('home/', include('fhblog.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('fhauthsystem.urls')),
    path('emails/', include('fhemails.urls'))
]

#TURN ON/OFF APP - fhapipage 
if 'fhapipage' in settings.INSTALLED_APPS:
    urlpatterns += path('api/', include('fhapipage.urls'), name='fhapipage'),


urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)