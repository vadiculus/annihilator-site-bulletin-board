from django.apps import AppConfig
from django.core.signals import Signal
from .tasks import send_activation_email_task

register_signal = Signal()

def register_dipatcher(sender, **kwargs):
    print(kwargs['instance'].id)
    send_activation_email_task.delay(kwargs['instance'].id)

register_signal.connect(register_dipatcher)

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
