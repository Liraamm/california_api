from django.db import models
from slugify import slugify


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True,
                             verbose_name='Название категории')
    slug = models.SlugField(max_length=30, primary_key=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(verbose_name='Название', max_length=30)
    description = models.CharField(verbose_name='Описание', max_length=100)
    description2 = models.CharField(verbose_name='Описание2', max_length=100)
    image = models.ImageField(
        upload_to='images/', blank=True, verbose_name='Изображение')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
