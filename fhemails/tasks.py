from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def send_email_task():
    send_mail('Foodhunterki Newsletter',
        'foodhunterki@foodhunterki.com',
    )

    return None