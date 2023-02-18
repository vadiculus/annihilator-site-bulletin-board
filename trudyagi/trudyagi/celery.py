from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trudyagi.settings')

app = Celery('trudyagi')

app.config_from_object('django.conf:settings', 'CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: ', self.request)