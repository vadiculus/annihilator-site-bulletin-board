from django.core.mail import send_mail
from django.core.signing import Signer
from trudyagi.settings import ALLOWED_HOSTS
from django.template.loader import render_to_string

signer = Signer()