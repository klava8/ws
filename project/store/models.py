from django.db import models

# Create your models here.


CATEGORY = [
    ('guppy', 'Гуппи'),
    ('carps', 'Карпы'),
    ('perches', 'Окуни'),
    ('pike', 'Щуки'),
]


class Product(models.Model):
    name = models.CharField(
        verbose_name='Наименование товара',
        max_length=255,
    )
    price = models.FloatField(
        verbose_name='Цена товара'
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='#'
        )
    
    def __str__(self):
        return self.name
    
    def full(self):
        return self.name + ' ' + self.price + ' ' + self.category + 'br' + self.image

class Category(models.Model):
    category = models.CharField(
        max_length=125,
        choices=CATEGORY,
        verbose_name='Категория'
    )

    def __str__(self):
        return self.category