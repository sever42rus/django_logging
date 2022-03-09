from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    price = models.PositiveIntegerField(verbose_name='Цена')
    categorys = models.ManyToManyField(to=Category, related_name='products', verbose_name='Категории')

    def __str__(self) -> str:
        return self.title
