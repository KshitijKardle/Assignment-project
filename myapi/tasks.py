from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email, username):
    subject = "Welcome to Our Platform!"
    message = f"Hello {username},\n\nThank you for registering."
    from_email = None
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
