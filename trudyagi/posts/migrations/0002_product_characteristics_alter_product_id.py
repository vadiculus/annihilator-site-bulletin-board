# Generated by Django 4.0.2 on 2023-02-23 14:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='characteristics',
            field=models.JSONField(blank=True, null=True, verbose_name='Характеристики'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0b2b31fb-0970-4be9-8e63-f1024a36356e'), editable=False, primary_key=True, serialize=False),
        ),
    ]
