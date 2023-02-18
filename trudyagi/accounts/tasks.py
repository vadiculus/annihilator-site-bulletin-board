from celery import shared_task
from django.core.mail import send_mail
from django.core.signing import Signer
from trudyagi.settings import ALLOWED_HOSTS
from django.template.loader import render_to_string
from .utilites import signer
from trudyagi.celery import app

@app.task
def send_activation_email_task(user_id):
    from .models import User
    user = User.objects.get(pk=user_id)
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://127.0.0.1:8000'

    context = {'host': host, 'user': user, 'sign': signer.sign(user.username)}
    print(context)
    subject = render_to_string('accounts/activation_account_subject.txt', context=context)
    body = render_to_string('accounts/activation_account_body.txt', context=context)
    user.email_user(subject, body)