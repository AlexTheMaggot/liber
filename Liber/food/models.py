from django.db import models


class Tag(models.Model):
    name = models.CharField(verbose_name='Название тега: ', max_length=200)
    slug_tag = models.SlugField(unique=True)
    img = models.ImageField(verbose_name='Изображение: ', upload_to='static/img/food/tags/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Restaurant(models.Model):
    name = models.CharField(verbose_name='Название ресторана: ', max_length=200)
    slug_restaurant = models.SlugField(unique=True)
    img = models.ImageField(verbose_name='Изображение: ', upload_to='static/img/food/restaurants/')
    description = models.TextField(verbose_name='Описание: ')
    rating = models.DecimalField(verbose_name='Рейтинг: ', max_digits=2, decimal_places=1)
    time_delivery = models.IntegerField(verbose_name='Время доставки: ')
    tags = models.ManyToManyField('Tag', verbose_name='Теги: ', related_name='tag')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'


class DishCategory(models.Model):
    name = models.CharField(verbose_name='Название категории: ', max_length=200)
    slug_dishcategory = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория блюд'
        verbose_name_plural = 'Категории блюд'


class Dish(models.Model):
    name = models.CharField(verbose_name='Название блюда: ', max_length=200)
    slug_dish = models.SlugField(unique=True)
    img = models.ImageField(verbose_name='Изображение: ', upload_to='static/img/food/dishes/')
    description = models.TextField(verbose_name='Описание: ')
    restaurant = models.ForeignKey('Restaurant', verbose_name='Ресторан: ', related_name='restaurant',
                                   on_delete=models.PROTECT)
    category = models.ForeignKey('DishCategory', verbose_name='Категория блюда', related_name='category',
                                 on_delete=models.PROTECT)
    available = models.BooleanField(verbose_name='В наличии')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'