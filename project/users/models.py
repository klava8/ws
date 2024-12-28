from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    goods_basket = models.ManyToManyField(
        to='store.Product',
        verbose_name='Корзина'
    )

class Wallet(models.Model):
    profile = models.ForeignKey(
        to=Profile,
        verbose_name='Пользователь',
        related_name='wallets',
        on_delete=models.CASCADE
    )
    money = models.FloatField(
        verbose_name='Сумма денег',
    )