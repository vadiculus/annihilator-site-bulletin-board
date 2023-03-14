from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.views.generic import CreateView

from accounts.models import User
from .utils import slugify
from django.urls import reverse
import uuid

class Product(models.Model):
    PRODUCT_CONDITION_CHOICE = (
        ('n', 'Новый'),
        ('u', 'Б/у'),
    )
    SALE_TYPE_CHOICE  = (
        ('s', 'Продажа'),
        ('e', 'Обмен'),
        ('f', 'Даром')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=70, verbose_name='Имя продукта')
    image = models.ImageField(upload_to='products-images/%Y/%m/%d', verbose_name='Изображение продукта')
    about = models.TextField(null=True, blank=True, verbose_name='О продукте')
    condition = models.CharField(max_length=5, default='n', choices=PRODUCT_CONDITION_CHOICE, verbose_name='Состояние товара')
    sale_type = models.CharField(max_length=5, default='s', choices=SALE_TYPE_CHOICE, verbose_name='Тип продажи')
    price = models.DecimalField(null=True,max_digits=8,decimal_places=2, verbose_name='Цена')
    attributes = models.JSONField(null=True, blank=True,verbose_name='Характеристики')
    characteristics = models.JSONField(null=True, blank=True,verbose_name='Дополнительные характеристики')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='products')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Категория', related_name='products')
    rating = models.FloatField(null=True, blank=True, verbose_name='Рейтинг', validators=[MaxValueValidator(5), MinValueValidator(0)])
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.sale_type in ['e', 'f']:
            self.price = 0
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:product_detail', args=[self.id])

    class Meta:
        ordering = ['-created']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        indexes = [
            models.Index(fields=["attributes"]),
            models.Index(fields=["price"]),
            models.Index(fields=["name"]),
            models.Index(fields=["name","attributes"])
        ]

class Product_Image(models.Model):
    image = models.ImageField(upload_to='products-images/%Y/%m/%d')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продуктов'

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя автора')
    content = models.TextField(verbose_name='Коомментарий')
    review = models.FloatField(verbose_name='Отзыв', validators=[MaxValueValidator(5), MinValueValidator(0)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    def save(self, commit=True, *args, **kwargs):
        if commit:
            author_comments = self.__class__.objects.filter(author=self.author, product=self.product)
        if author_comments:
            author_comments.delete()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    slug = models.SlugField()
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT, verbose_name='Рубрика', related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Rubric(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название рубрики')
    slug = models.SlugField()
    image = models.ImageField(upload_to='rubric-images/', verbose_name='Изображение рубрики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
