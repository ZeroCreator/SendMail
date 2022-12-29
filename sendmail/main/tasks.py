from django.core.mail import send_mail
from sendmail.celery import app

from .service import send
from .models import Contact

@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на рассылку.',
            'Мы будем присылать вам много спама.',
            'shkola.olga@gmail.com',
            [contact.email],
            fail_silently=False,
        )
