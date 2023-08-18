from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    decrp = models.CharField(max_length=100, verbose_name='описание')
    img = models.ImageField(upload_to='products/', verbose_name='изображение', null=True, blank=True)
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    data = models.DateTimeField(verbose_name='дата')
    data_chg = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name = 'продукты'


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    decrp = models.CharField(max_length=100, verbose_name='описание')
    created_at = models.IntegerField(verbose_name='создан', null=True, blank=True)

