# Generated by Django 4.0.2 on 2023-02-22 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_actived'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_actived',
        ),
    ]
