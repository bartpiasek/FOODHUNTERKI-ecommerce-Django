from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_email_task

# Create your views here.
def email_sender(request):
    send_email_task()
    return HttpResponse('Wysłane!')
    