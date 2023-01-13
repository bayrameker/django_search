from django.db import models

# Create your models here.
from app.enum import Currency


class Coin(models.Model):
    name = models.CharField(max_length=30)


class Price(models.Model):
    currency = models.CharField(max_length=30, choices=Currency.choices, default=Currency.USD)
    coin = models.ForeignKey(to=Coin, on_delete=models.CASCADE)
    price = models.FloatField()
    transactionAt = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
