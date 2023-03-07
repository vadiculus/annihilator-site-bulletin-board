# Generated by Django 4.0.2 on 2023-03-07 22:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_product_attributes_alter_product_characteristics_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('110b0a17-ee90-4878-ba44-35d44802b276'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['attributes'], name='posts_produ_attribu_05bfad_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['price'], name='posts_produ_price_a2323d_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='posts_produ_name_a67e54_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name', 'attributes'], name='posts_produ_name_b16759_idx'),
        ),
    ]