from django.db import models


class Category(models.Model):

    cat = models.CharField(max_length=100, verbose_name='категория')
    decrp = models.CharField(max_length=100, verbose_name='описание')
    created_at = models.IntegerField(verbose_name='создан', null=True, blank=True)

    def __str__(self):
        return f'{self.cat}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    decrp = models.CharField(max_length=100, verbose_name='описание')
    img = models.ImageField(upload_to='database/', verbose_name='изображение', null=True, blank=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена')
    data = models.DateTimeField(verbose_name='дата')
    data_chg = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):

    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.CharField(max_length=100, verbose_name='number')
    title = models.CharField(max_length=100, verbose_name='название')
    active = models.BooleanField(default=True, verbose_name='active')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'





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


