from django.db import models

from main.models import Product


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

def __str__(self):
    return f'{self.product.name} v.{self.number}'

