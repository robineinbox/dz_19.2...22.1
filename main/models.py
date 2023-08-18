from django.db import models
import datetime

# Объявление словаря NULLABLE
NULLABLE = {'null': True, 'blank': True}

class MainCategory(models.Model):
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.description


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='категория')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    # image = models.ImageField(verbose_name='изображение (превью)', **NULLABLE)
    image = models.ImageField(verbose_name='изображение (превью)', upload_to='images/', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_price = models.IntegerField(verbose_name='цена за покупку')
    produce_day = models.DateField(verbose_name='дата создания', default=datetime.date(2022, 1, 1))
    last_change = models.DateField(verbose_name='дата последнего изменения', auto_now=True)


    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

class Contacts(models.Model):
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    address = models.CharField(max_length=100, verbose_name='адрес')
    phone_number = models.CharField(max_length=20, verbose_name='номер телефона')
    email = models.EmailField(verbose_name='адрес электронной почты')

    def __str__(self):
        return f'{self.country}, {self.city}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

class YourModel(models.Model):
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.url
