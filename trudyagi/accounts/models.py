from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    icon = models.ImageField(upload_to='profile-icons/', null=True, blank=True, verbose_name='Фото пользователя')
    about = models.TextField(null=True, blank=True, verbose_name='О себе')
    contacts = models.EmailField(null=True, blank=True, verbose_name='Контактный email')
    rating = models.FloatField(null=True, blank=True)

