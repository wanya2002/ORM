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
        verbose_name_plural = 'продукты'


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    decrp = models.CharField(max_length=100, verbose_name='описание')
    created_at = models.IntegerField(verbose_name='создан', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Blog(models.Model):

    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    content = models.TextField(verbose_name='содержимое')
    prv = models.ImageField(upload_to='products/', verbose_name='изображение', null=True, blank=True)
    data = models.DateTimeField(verbose_name='дата')
    publish = models.BooleanField(default=True, verbose_name='Опубликовано')
    count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


