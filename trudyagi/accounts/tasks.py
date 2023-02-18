from celery import shared_task
from django.core.mail import send_mail
from django.core.signing import Signer
from trudyagi.settings import ALLOWED_HOSTS
from django.template.loader import render_to_string
from .utilites import signer
from trudyagi.celery import app
from trudyagi import config

@app.task
def send_activation_email_task(email, username):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://127.0.0.1:8000'

    context = {'host': host, 'sign': signer.sign(username)}
    print(context)
    subject = render_to_string('accounts/activation_account_subject.txt', context=context)
    body = render_to_string('accounts/activation_account_body.txt', context=context)
    send_mail(subject, body, config.sptm_email, [email])