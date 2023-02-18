from django.apps import AppConfig
from django.core.signals import Signal

class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
