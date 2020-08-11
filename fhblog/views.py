from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    context = {'posts':posts}
    return render(request, 'fhblog/blog.html', context)

def about(request):
    return render(request, 'fhblog/about.html')

