from django.db import models
from posts.models import Product
from accounts.models import User

class Order(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author_orders', verbose_name='Отправитель')
    seller = models.ForeignKey(User, on_delete=models.PROTECT, related_name='seller_orders', verbose_name='Продавец')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_orders', verbose_name='Продукт')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    country = models.CharField(max_length=200, verbose_name='Страна')
    city = models.CharField(max_length=200, verbose_name='Город')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый индекс')
    additional_information = models.TextField(null=True, blank=True, verbose_name='Дополнительная информация')
    read = models.BooleanField(default=False, verbose_name='Прочитано')
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(verbose_name='Количество')
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Полная Цена')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
